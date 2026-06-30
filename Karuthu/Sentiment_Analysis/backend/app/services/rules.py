from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

from app.services.preprocess import TextPreprocessor


class RuleEngine:

    model = SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    POSITIVE_PHRASES = [
        # Overall Experience
        "excellent service","excellent experience","great experience","wonderful experience","pleasant experience","very satisfied","highly satisfied","completely satisfied","extremely satisfied","happy with service","happy with treatment","overall excellent","overall very good","overall satisfied","excellent hospital","good hospital","highly recommend this hospital",
        # Doctors
        "doctor was good","doctor was excellent","doctor was professional","doctor explained clearly","doctor explained everything","doctor was friendly","doctor was caring","doctor was knowledgeable","doctor was supportive","doctor treated me well","doctors are good","excellent doctors","best doctors","experienced doctor",
        # Nurses
        "nurse was caring","nurse was helpful","nurses were good","nurses were supportive","nurses responded quickly","nurses were polite","nurses took good care","excellent nursing care","friendly nurses",
        # Treatment
        "treatment was excellent","treatment was very good","treatment was successful","treatment was effective","treatment was good","received proper treatment","quality treatment","excellent medical care","received excellent care",
        # Staff
        "staff was helpful","staff was friendly","staff was professional","staff was polite","staff was cooperative","staff was courteous","support staff was excellent","excellent customer service",
        # Billing
        "billing was quick","Registration was quick","billing process was easy","billing was accurate","billing was transparent",
        # Waiting Time
        "no waiting time","short waiting time","quick service","fast service","prompt service","appointment was on time",
        # Cleanliness
        "hospital was clean","room was clean","washroom was clean","clean environment","well maintained hospital","excellent hygiene","very clean facility",
        # Food
        "food was good","food was tasty","food quality was good","healthy food",
        # Facilities
        "excellent facilities","good facilities","comfortable room","comfortable stay","good infrastructure","modern equipment",
        # Emergency
        "emergency service was excellent","emergency response was quick","ambulance arrived quickly","medicine was available","pharmacy service was quick","pharmacy staff was helpful",
        #Discharge
        "discharge was quick","excellent","very good","good","awesome","amazing","outstanding","fantastic","superb","perfect","excellent care","great care","highly appreciated","thank you","thank you doctor","thank you nurses","keep up the good work"
    ]

    NEGATIVE_PHRASES = [
        "too expensive","very expensive","costly treatment","treatment was expensive","high treatment cost","high hospital charges","high medical expenses","overpriced","billing was too high","unexpected charges","hidden charges","unnecessary charges","extra charges","billing issue","billing error","billing took too long","waiting time was too long","long waiting time","very long waiting time","too much waiting","waited for hours","waited a long time",
        "took too much time","took longer than expected","service was delayed","treatment was delayed","doctor came late","doctor was late","nurse response was slow","staff response was slow","slow service","slow response","late response","delayed admission","delayed discharge","delayed consultation","appointment was delayed","discharge process was slow","registration took too long","admission process was slow","billing process was slow","pharmacy service was slow",
        "laboratory results were delayed","test results were delayed","queue was too long","long queue","crowded hospital","too crowded","wasted my time","waste of time","poor time management","staff shortage caused delay","doctor was unavailable","service needs improvement","hospital needs improvement","very disappointing","poor experience","bad experience","Room was dirty.","Bedsheets were not changed.","Washroom was unhygienic.","Long waiting despite emergency.",
        "Nurses responded slowly.","Doctor did not visit regularly.","Food was cold.","Food quality was poor.","Discharge took too long.","Room AC was not working.","Water leakage in the room.","Medicine was unavailable.","Patient care was poor.","Noise disturbed patients.","Housekeeping was poor.","Hospital charges were too high.","Billing was incorrect.","Room was not cleaned.","Staff ignored patient requests.","Hospital was overcrowded.","Long discharge process.","Need improvement in emergency services.",
        "Emergency response was slow.","Patient waited too long.","Doctor was unavailable.","Nurses were slow.","Emergency room was crowded.","No beds available.","Treatment was delayed.","Ambulance arrived late.","Poor emergency management.","Emergency staff was rude.","Life-saving equipment was unavailable.","Delay in diagnosis.","Patient was unattended.","Communication was poor.","Hospital was not prepared.","Emergency room was dirty.","Very disappointing emergency care.","Critical patient was delayed."
    ]

    NEUTRAL_PHRASES = [
        "no comments","no comment","nothing unusual","nothing to say","nothing special","nothing much","n/a","na","nil","none","-","ok","okay","fine","treatment was acceptable","treatment was average","hospital was okay","hospital was fine","hospital was average","hospital was satisfactory","hospital was acceptable",
        "average","normal","acceptable","adequate","satisfactory","standard","routine","fair","fair enough","decent","reasonable","ordinary","usual","as expected","met expectations","overall okay","overall fine","overall average","overall satisfactory","it was okay","it was fine","it was average","it was satisfactory","it was acceptable",
        "overall acceptable","everything was okay","billing was confusing","everything was fine","everything was normal","everything was satisfactory","everything was acceptable","service was okay","service was fine","service was average","service was satisfactory","service was acceptable","treatment was okay","treatment was fine","treatment was satisfactory",
        "room was okay","room was fine","room was adequate","room was acceptable","room was average","waiting time was acceptable","waiting time was manageable","waiting time was reasonable","staff was okay","staff was polite","staff was professional","doctor was okay","doctor explained properly","doctor was professional","nurses were okay",
        "facilities were adequate","bad smell","facilities were acceptable","facilities were standard","facilities met expectations","nothing to complain","nothing to mention","no issues","no major issues","no major complaints","experience was okay","experience was average","experience was normal","experience was satisfactory","experience was acceptable"
    ]
    
    positive_embeddings = model.encode(
        POSITIVE_PHRASES,
        convert_to_numpy=True
    )

    negative_embeddings = model.encode(
        NEGATIVE_PHRASES,
        convert_to_numpy=True
    )

    neutral_embeddings = model.encode(
        NEUTRAL_PHRASES,
        convert_to_numpy=True
    )

    @classmethod
    def predict(cls, text):

        text = TextPreprocessor.process(text)

        query_embedding = cls.model.encode(
            text,
            convert_to_numpy=True
        )

        pos_score = cosine_similarity(
            [query_embedding],
            cls.positive_embeddings
        ).max()

        neg_score = cosine_similarity(
            [query_embedding],
            cls.negative_embeddings
        ).max()

        neu_score = cosine_similarity(
            [query_embedding],
            cls.neutral_embeddings
        ).max()

        scores = {
            "positive": pos_score,
            "negative": neg_score,
            "neutral": neu_score
        }

        sentiment = max(
            scores,
            key=scores.get
        )

        confidence = scores[sentiment]

        if confidence < 0.80:
            return None

        return {
            "positive": round(float(pos_score), 4),
            "neutral": round(float(neu_score), 4),
            "negative": round(float(neg_score), 4),
            "sentiment": sentiment,
            "confidence": round(float(confidence), 4),
            "source": "semantic_rule_engine"
        }