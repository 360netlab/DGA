import sys
import argparse
import hashlib
import time

prefix = ["cam", "video", "x", "a", "www", "ftp", "ssl", "tftp", "www1",
            "www2", "noc", "smtp", "pop", "ssl", "secure", "images", "th",
            "img", "download", "mail", "remote", "blog", "webmail", "server",
            "ns1", "vpn", "m", "shop", "mail2", "test", "ww1", "support", "dev",
            "web", "bbs", "email", "cloud", "gw", "admin", "news"]

verbs = ["be", "have", "do", "say", "go", "get", "make", "know", "think",
            "take", "see", "come", "want", "look", "use", "find", "give",
            "tell", "work", "call", "try", "ask", "need", "feel", "become",
            "leave", "put", "mean", "keep", "let", "begin", "seem", "help",
            "talk", "turn", "start", "show", "hear", "play", "run", "move",
            "like", "live", "believe", "hold", "bring", "happen", "write",
            "provide", "sit", "stand", "lose", "pay", "meet", "include",
            "continue", "set", "learn", "change", "lead", "understand",
            "watch", "follow", "stop", "create", "speak", "read", "allow",
            "add", "spend", "grow", "open", "walk", "win", "offer", "remember",
            "love", "consider", "appear", "buy", "wait", "serve", "die",
            "send", "expect", "build", "stay", "fall", "cut", "reach",
            "kill", "remain", "suggest", "raise", "pass", "sell", "require",
            "report", "decide", "pull" ]

adjs = ["able", "acceptable", "according", "accurate", "action", "active",
            "actual", "additional", "administrative", "adult", "afraid",
            "after", "afternoon", "agent", "aggressive", "ago", "airline",
            "alive", "all", "alone", "alternative", "amazing", "angry",
            "animal", "annual", "another", "anxious", "any", "apart",
            "appropriate", "asleep", "automatic", "available", "aware", "away",
            "background", "basic", "beautiful", "beginning", "best", "better",
            "big", "bitter", "boring", "born", "both", "brave", "brief",
            "bright", "brilliant", "broad", "brown", "budget", "business",
            "busy", "calm", "capable", "capital", "car", "careful", "certain",
            "chance", "character", "cheap", "chemical", "chicken", "choice",
            "civil", "classic", "clean", "clear", "close", "cold",
            "comfortable", "commercial", "common", "competitive", "complete",
            "complex", "comprehensive", "confident", "connect", "conscious",
            "consistent", "constant", "content", "cool", "corner", "correct",
            "crazy", "creative", "critical", "cultural", "curious", "current",
            "cute", "dangerous", "dark", "daughter", "day", "dead", "dear",
            "decent", "deep", "dependent", "designer", "desperate", "different",
            "difficult", "direct", "dirty", "distinct", "double", "downtown",
            "dramatic", "dress", "drunk", "dry", "due", "each", "east",
            "eastern", "easy", "economy", "educational", "effective",
            "efficient", "either", "electrical", "electronic", "embarrassed",
            "emergency", "emotional", "empty", "enough", "entire",
            "environmental", "equal", "equivalent", "even", "evening", "every",
            "exact", "excellent", "exciting", "existing", "expensive", "expert",
            "express", "extension", "external", "extra", "extreme", "fair",
            "false", "familiar", "famous", "far", "fast", "fat", "federal",
            "feeling", "female", "few", "final", "financial", "fine", "firm",
            "first", "fit", "flat", "foreign", "formal", "former", "forward",
            "free", "frequent", "fresh", "friendly", "front", "full", "fun",
            "funny", "future", "game", "general", "glad", "glass", "global",
            "gold", "good", "grand", "great", "green", "gross", "guilty", "happy",
            "hard", "head", "healthy", "heavy", "helpful", "high", "his",
            "historical", "holiday", "home", "honest", "horror", "hot", "hour",
            "house", "huge", "human", "hungry", "ideal", "ill", "illegal",
            "immediate", "important", "impossible", "impressive", "incident",
            "independent", "individual", "inevitable", "informal", "initial",
            "inner", "inside", "intelligent", "interesting", "internal",
            "international", "joint", "junior", "just", "key", "kind", "kitchen",
            "known", "large", "last", "late", "latter", "leading", "least",
            "leather", "left", "legal", "less", "level", "life", "little", "live",
            "living", "local", "logical", "lonely", "long", "loose", "lost",
            "loud", "low", "lower", "lucky", "mad", "main", "major", "male",
            "many", "massive", "master", "material", "maximum", "mean", "medical",
            "medium", "mental", "middle", "minimum", "minor", "minute", "mission",
            "mobile", "money", "more", "most", "mother", "motor", "mountain",
            "much", "narrow", "nasty", "national", "native", "natural", "nearby",
            "neat", "necessary", "negative", "neither", "nervous", "new", "next",
            "nice", "normal", "north", "novel", "numerous", "objective",
            "obvious", "odd", "official", "ok", "old", "only", "open", "opening",
            "opposite", "ordinary", "original", "other", "otherwise", "outside",
            "over", "overall", "own", "parking", "particular", "party", "past",
            "patient", "perfect", "period", "personal", "physical", "plane",
            "plastic", "pleasant", "plenty", "plus", "political", "poor",
            "popular", "positive", "possible", "potential", "powerful",
            "practical", "pregnant", "present", "pretend", "pretty", "previous",
            "primary", "prior", "private", "prize", "professional", "proof",
            "proper", "proud", "psychological", "public", "pure", "purple",
            "quick", "quiet", "rare", "raw", "ready", "real", "realistic",
            "reasonable", "recent", "red", "regular", "relative", "relevant",
            "remarkable", "remote", "representative", "resident", "responsible",
            "rich", "right", "rough", "round", "routine", "royal", "sad", "safe",
            "salt", "same", "savings", "scared", "sea", "secret", "secure",
            "select", "senior", "sensitive", "separate", "serious", "several",
            "severe", "sexual", "sharp", "short", "shot", "sick", "signal",
            "significant", "silly", "silver", "similar", "simple", "single",
            "slight", "slow", "small", "smart", "smooth", "soft", "solid", "some",
            "sorry", "south", "southern", "spare", "special", "specialist",
            "specific", "spiritual", "square", "standard", "status", "still",
            "stock", "straight", "strange", "street", "strict", "strong", "stupid",
            "subject", "substantial", "successful", "such", "sudden", "sufficient",
            "suitable", "super", "sure", "suspicious", "sweet", "swimming", "tall",
            "technical", "temporary", "terrible", "that", "then", "these", "thick",
            "thin", "think", "this", "tight", "time", "tiny", "top", "total", "tough",
            "traditional", "training", "trick", "true", "typical", "ugly", "unable",
            "unfair", "unhappy", "unique", "united", "unlikely", "unusual",
            "upper", "upset", "upstairs", "used", "useful", "usual", "valuable",
            "various", "vast", "vegetable", "visible", "visual", "warm", "waste",
            "weak", "weekly", "weird", "west", "western", "what", "which", "white",
            "whole", "wide", "wild", "willing", "wine", "winter", "wise",
            "wonderful", "wooden", "work", "working", "worth", "wrong",
            "yellow", "young"]

nouns = ["a", "ability", "abroad", "abuse", "access", "accident", "account",
            "act", "action", "active", "activity", "actor", "ad", "addition",
            "address", "administration", "adult", "advance", "advantage",
            "advertising", "advice", "affair", "affect", "afternoon", "age",
            "agency", "agent", "agreement", "air", "airline", "airport",
            "alarm", "alcohol", "alternative", "ambition", "amount",
            "analysis", "analyst", "anger", "angle", "animal", "annual",
            "answer", "anxiety", "anybody", "anything", "anywhere",
            "apartment", "appeal", "appearance", "apple", "application",
            "appointment", "area", "argument", "arm", "army", "arrival",
            "art", "article", "aside", "ask", "aspect", "assignment", "assist",
            "assistance", "assistant", "associate", "association", "assumption",
            "atmosphere", "attack", "attempt", "attention", "attitude",
            "audience", "author", "average", "award", "awareness", "baby",
            "back", "background", "bad", "bag", "bake", "balance", "ball",
            "band", "bank", "bar", "base", "baseball", "basis", "basket", "bat",
            "bath", "bathroom", "battle", "beach", "bear", "beat", "beautiful",
            "bed", "bedroom", "beer", "beginning", "being", "bell", "belt",
            "bench", "bend", "benefit", "bet", "beyond", "bicycle", "bid",
            "big", "bike", "bill", "bird", "birth", "birthday", "bit", "bite",
            "bitter", "black", "blame", "blank", "blind", "block", "blood",
            "blow", "blue", "board", "boat", "body", "bone", "bonus", "book",
            "boot", "border", "boss", "bother", "bottle", "bottom", "bowl",
            "box", "boy", "boyfriend", "brain", "branch", "brave", "bread",
            "break", "breakfast", "breast", "breath", "brick", "bridge", "brief",
            "brilliant", "broad", "brother", "brown", "brush", "buddy", "budget",
            "bug", "building", "bunch", "burn", "bus", "business", "button",
            "buy", "buyer", "cabinet", "cable", "cake", "calendar", "call",
            "calm", "camera", "camp", "campaign", "can", "cancel", "cancer",
            "candidate", "candle", "candy", "cap", "capital", "car", "card",
            "care", "career", "carpet", "carry", "case", "cash", "cat", "catch",
            "category", "cause", "celebration", "cell", "chain", "chair",
            "challenge", "champion", "championship", "chance", "change",
            "channel", "chapter", "character", "charge", "charity", "chart",
            "check", "cheek", "chemical", "chemistry", "chest", "chicken",
            "child", "childhood", "chip", "chocolate", "choice", "church",
            "cigarette", "city", "claim", "class", "classic", "classroom",
            "clerk", "click", "client", "climate", "clock", "closet", "clothes",
            "cloud", "club", "clue", "coach", "coast", "coat", "code", "coffee",
            "cold", "collar", "collection", "college", "combination", "combine",
            "comfort", "comfortable", "command", "comment", "commercial",
            "commission", "committee", "common", "communication", "community",
            "company", "comparison", "competition", "complaint", "complex",
            "computer", "concentrate", "concept", "concern", "concert",
            "conclusion", "condition", "conference", "confidence", "conflict",
            "confusion", "connection", "consequence", "consideration", "consist",
            "constant", "construction", "contact", "contest", "context",
            "contract", "contribution", "control", "conversation", "convert",
            "cook", "cookie", "copy", "corner", "cost", "count", "counter",
            "country", "county", "couple", "courage", "course", "court", "cousin",
            "cover", "cow", "crack", "craft", "crash", "crazy", "cream",
            "creative", "credit", "crew", "criticism", "cross", "cry", "culture",
            "cup", "currency", "current", "curve", "customer", "cut", "cycle",
            "damage", "dance", "dare", "dark", "data", "database", "date",
            "daughter", "day", "dead", "deal", "dealer", "dear", "death",
            "debate", "debt", "decision", "deep", "definition", "degree",
            "delay", "delivery", "demand", "department", "departure", "dependent",
            "deposit", "depression", "depth", "description", "design",
            "designer", "desire", "desk", "detail", "development", "device",
            "devil", "diamond", "diet", "difference", "difficulty", "dig",
            "dimension", "dinner", "direction", "director", "dirt", "disaster",
            "discipline", "discount", "discussion", "disease", "dish", "disk",
            "display", "distance", "distribution", "district", "divide",
            "doctor", "document", "dog", "door", "dot", "double", "doubt",
            "draft", "drag", "drama", "draw", "drawer", "drawing", "dream",
            "dress", "drink", "drive", "driver", "drop", "drunk", "due", "dump",
            "dust", "duty", "ear", "earth", "ease", "east", "eat", "economics",
            "economy", "edge", "editor", "education", "effect", "effective",
            "efficiency", "effort", "egg", "election", "elevator", "emergency",
            "emotion", "emphasis", "employ", "employee", "employer", "employment",
            "end", "energy", "engine", "engineer", "engineering", "entertainment",
            "enthusiasm", "entrance", "entry", "environment", "equal", "equipment",
            "equivalent", "error", "escape", "essay", "establishment", "estate",
            "estimate", "evening", "event", "evidence", "exam", "examination",
            "example", "exchange", "excitement", "excuse", "exercise", "exit",
            "experience", "expert", "explanation", "expression", "extension",
            "extent", "external", "extreme", "eye", "face", "fact", "factor",
            "fail", "failure", "fall", "familiar", "family", "fan", "farm",
            "farmer", "fat", "father", "fault", "fear", "feature", "fee", "feed",
            "feedback", "feel", "feeling", "female", "few", "field", "fight",
            "figure", "file", "fill", "film", "final", "finance", "finding",
            "finger", "finish", "fire", "fish", "fishing", "fix", "flight",
            "floor", "flow", "flower", "fly", "focus", "fold", "following",
            "food", "foot", "football", "force", "forever", "form", "formal",
            "fortune", "foundation", "frame", "freedom", "friend", "friendship",
            "front", "fruit", "fuel", "fun", "function", "funeral", "funny",
            "future", "gain", "game", "gap", "garage", "garbage", "garden",
            "gas", "gate", "gather", "gear", "gene", "general", "gift", "girl",
            "girlfriend", "give", "glad", "glass", "glove", "go", "goal",
            "god", "gold", "golf", "good", "government", "grab", "grade",
            "grand", "grandfather", "grandmother", "grass", "great", "green",
            "grocery", "ground", "group", "growth", "guarantee", "guard",
            "guess", "guest", "guidance", "guide", "guitar", "guy",
            "habit", "hair", "half", "hall", "hand", "handle", "hang",
            "harm", "hat", "hate", "head", "health", "hearing", "heart",
            "heat", "heavy", "height", "hell", "hello", "help", "hide",
            "high", "highlight", "highway", "hire", "historian", "history",
            "hit", "hold", "hole", "holiday", "home", "homework", "honey",
            "hook", "hope", "horror", "horse", "hospital", "host", "hotel",
            "hour", "house", "housing", "human", "hunt", "hurry", "hurt",
            "husband", "ice", "idea", "ideal", "if", "illegal", "image",
            "imagination", "impact", "implement", "importance", "impress",
            "impression", "improvement", "incident", "income", "increase",
            "independence", "independent", "indication", "individual",
            "industry", "inevitable", "inflation", "influence", "information",
            "initial", "initiative", "injury", "insect", "inside",
            "inspection", "inspector", "instance", "instruction",
            "insurance", "intention", "interaction", "interest",
            "internal", "international", "internet", "interview",
            "introduction", "investment", "invite", "iron", "island",
            "issue", "it", "item", "jacket", "job", "join", "joint", "joke",
            "judge", "judgment", "juice", "jump", "junior", "jury", "keep",
            "key", "kick", "kid", "kill", "kind", "king", "kiss", "kitchen",
            "knee", "knife", "knowledge", "lab", "lack", "ladder", "lady",
            "lake", "land", "landscape", "language", "laugh", "law", "lawyer",
            "lay", "layer", "lead", "leader", "leadership", "leading",
            "league", "leather", "leave", "lecture", "leg", "length",
            "lesson", "let", "letter", "level", "library", "lie", "life",
            "lift", "light", "limit", "line", "link", "lip", "list", "listen",
            "literature", "living", "load", "loan", "local", "location",
            "lock", "log", "long", "look", "loss", "love", "low", "luck",
            "lunch", "machine", "magazine", "mail", "main", "maintenance",
            "major", "make", "male", "mall", "man", "management", "manager",
            "manner", "manufacturer", "many", "map", "march", "mark",
            "market", "marketing", "marriage", "master", "match", "mate",
            "material", "math", "matter", "maximum", "maybe", "meal",
            "meaning", "measurement", "meat", "media", "medicine", "medium",
            "meet", "meeting", "member", "membership", "memory", "mention",
            "menu", "mess", "message", "metal", "method", "middle", "midnight",
            "might", "milk", "mind", "mine", "minimum", "minor", "minute",
            "mirror", "miss", "mission", "mistake", "mix", "mixture", "mobile",
            "mode", "model", "mom", "moment", "money", "monitor", "month", "mood",
            "morning", "mortgage", "most", "mother", "motor", "mountain",
            "mouse", "mouth", "move", "movie", "mud", "muscle", "music",
            "nail", "name", "nasty", "nation", "national", "native", "natural",
            "nature", "neat", "necessary", "neck", "negative", "negotiation",
            "nerve", "net", "network", "news", "newspaper", "night", "nobody",
            "noise", "normal", "north", "nose", "note", "nothing", "notice",
            "novel", "number", "nurse", "object", "objective", "obligation",
            "occasion", "offer", "office", "officer", "official", "oil",
            "opening", "operation", "opinion", "opportunity", "opposite",
            "option", "orange", "order", "ordinary", "organization", "original",
            "other", "outcome", "outside", "oven", "owner", "pace", "pack",
            "package", "page", "pain", "paint", "painting", "pair", "panic",
            "paper", "parent", "park", "parking", "part", "particular",
            "partner", "party", "pass", "passage", "passenger", "passion",
            "past", "path", "patience", "patient", "pattern", "pause", "pay",
            "payment", "peace", "peak", "pen", "penalty", "pension", "people",
            "percentage", "perception", "performance", "period", "permission",
            "permit", "person", "personal", "personality", "perspective",
            "phase", "philosophy", "phone", "photo", "phrase", "physical",
            "physics", "piano", "pick", "picture", "pie", "piece", "pin",
            "pipe", "pitch", "pizza", "place", "plan", "plane", "plant",
            "plastic", "plate", "platform", "play", "player", "pleasure",
            "plenty", "poem", "poet", "poetry", "point", "police", "policy",
            "politics", "pollution", "pool", "pop", "population", "position",
            "positive", "possession", "possibility", "possible", "post", "pot",
            "potato", "potential", "pound", "power", "practice", "preference",
            "preparation", "presence", "present", "presentation", "president",
            "press", "pressure", "price", "pride", "priest", "primary",
            "principle", "print", "prior", "priority", "private", "prize",
            "problem", "procedure", "process", "produce", "product", "profession",
            "professional", "professor", "profile", "profit", "program",
            "progress", "project", "promise", "promotion", "prompt", "proof",
            "property", "proposal", "protection", "psychology", "public", "pull",
            "punch", "purchase", "purple", "purpose", "push", "put", "quality",
            "quantity", "quarter", "queen", "question", "quiet", "quit", "quote",
            "race", "radio", "rain", "raise", "range", "rate", "ratio",
            "raw", "reach", "reaction", "read", "reading", "reality", "reason",
            "reception", "recipe", "recognition", "recommendation", "record",
            "recording", "recover", "red", "reference", "reflection",
            "refrigerator", "refuse", "region", "register", "regret",
            "regular", "relation", "relationship", "relative", "release",
            "relief", "remote", "remove", "rent", "repair", "repeat",
            "replacement", "reply", "report", "representative", "republic",
            "reputation", "request", "requirement", "research", "reserve",
            "resident", "resist", "resolution", "resolve", "resort", "resource",
            "respect", "respond", "response", "responsibility", "rest",
            "restaurant", "result", "return", "reveal", "revenue", "review",
            "revolution", "reward", "rice", "rich", "ride", "ring", "rip",
            "rise", "risk", "river", "road", "rock", "role", "roll", "roof",
            "room", "rope", "rough", "round", "routine", "row", "royal",
            "rub", "ruin", "rule", "run", "rush", "sad", "safe", "safety",
            "sail", "salad", "salary", "sale", "salt", "sample", "sand",
            "sandwich", "satisfaction", "save", "savings", "scale", "scene",
            "schedule", "scheme", "school", "science", "score", "scratch",
            "screen", "screw", "script", "sea", "search", "season", "seat",
            "second", "secret", "secretary", "section", "sector", "security",
            "selection", "self", "sell", "senior", "sense", "sensitive",
            "sentence", "series", "serve", "service", "session", "set",
            "setting", "sex", "shake", "shame", "shape", "share", "she",
            "shelter", "shift", "shine", "ship", "shirt", "shock", "shoe",
            "shoot", "shop", "shopping", "shot", "shoulder", "show", "shower",
            "sick", "side", "sign", "signal", "signature", "significance",
            "silly", "silver", "simple", "sing", "singer", "single", "sink",
            "sir", "sister", "site", "situation", "size", "skill", "skin",
            "skirt", "sky", "sleep", "slice", "slide", "slip", "smell",
            "smile", "smoke", "snow", "society", "sock", "soft", "software",
            "soil", "solid", "solution", "somewhere", "son", "song", "sort",
            "sound", "soup", "source", "south", "space", "spare", "speaker",
            "special", "specialist", "specific", "speech", "speed", "spell",
            "spend", "spirit", "spiritual", "spite", "split", "sport",
            "spot", "spray", "spread", "spring", "square", "stable",
            "staff", "stage", "stand", "standard", "star", "start",
            "state", "statement", "station", "status", "stay", "steak",
            "steal", "step", "stick", "still", "stock", "stomach", "stop",
            "storage", "store", "storm", "story", "strain", "stranger",
            "strategy", "street", "strength", "stress", "stretch", "strike",
            "string", "strip", "stroke", "structure", "struggle", "student",
            "studio", "study", "stuff", "stupid", "style", "subject",
            "substance", "success", "suck", "sugar", "suggestion", "suit",
            "summer", "sun", "supermarket", "support", "surgery", "surprise",
            "surround", "survey", "suspect", "sweet", "swim", "swimming",
            "swing", "switch", "sympathy", "system", "table", "tackle", "tale",
            "talk", "tank", "tap", "target", "task", "taste", "tax", "tea",
            "teach", "teacher", "teaching", "team", "tear", "technology",
            "telephone", "television", "tell", "temperature", "temporary",
            "tennis", "tension", "term", "test", "text", "thanks", "theme",
            "theory", "thing", "thought", "throat", "ticket", "tie", "till",
            "time", "tip", "title", "today", "toe", "tomorrow", "tone",
            "tongue", "tonight", "tool", "tooth", "top", "topic", "total",
            "touch", "tough", "tour", "tourist", "towel", "tower", "town",
            "track", "trade", "tradition", "traffic", "train", "trainer",
            "training", "transition", "transportation", "trash", "travel",
            "treat", "tree", "trick", "trip", "trouble", "truck", "trust",
            "truth", "try", "tune", "turn", "twist", "type", "uncle",
            "understanding", "union", "unique", "unit", "university",
            "upper", "upstairs", "use", "user", "usual", "vacation",
            "valuable", "value", "variation", "variety", "vast", "vegetable",
            "vehicle", "version", "video", "view", "village", "virus",
            "visit", "visual", "voice", "volume", "wait", "wake", "walk",
            "wall", "war", "warning", "wash", "watch", "water", "wave", "way",
            "weakness", "wealth", "wear", "weather", "web", "wedding", "week",
            "weekend", "weight", "weird", "welcome", "west", "western", "wheel",
            "whereas", "while", "white", "whole", "wife", "will", "win",
            "wind", "window", "wine", "wing", "winner", "winter", "wish",
            "witness", "woman", "wonder", "wood", "word", "work", "worker",
            "working", "world", "worry", "worth", "wrap", "writer", "writing",
            "yard", "year", "yellow", "yesterday", "you", "young", "youth",
            "zone"]

TLDs = ["art", "click", "club", "com", "fans", "futbol", "in", "info",
            "link", "net", "nl", "observer", "one", "org", "pictures",
            "realty", "rocks", "tel", "top", "xyz"]


class domain_generator:
    def __init__(self, ts):
        global prefix
        global verbs
        global adjs
        global nouns
        global TLDs
        self.prefix = prefix
        self.verbs = verbs
        self.adjs = adjs
        self.nouns = nouns
        self.tlds = TLDs
        self.seed = self.init_seed(ts)

    def init_seed(self, ts):
        timea = time.localtime(ts)
        seed_str = time.strftime("%b %Y 00:00", timea)

        s = hashlib.sha256()
        s.update(seed_str)
        seed = int(s.hexdigest()[:8], 16)

        return seed

    def rand(self):
        x = self.seed ^ ((self.seed << 13) & 0xffffffff)
        y = x ^ (x >> 17)
        self.seed = (y ^ 32 * y) & 0xffffffff;

    def generate_domain(self):
        #c2 format: [prefix.]verbe[-]adj[-]noun.TLD
        domain = ''

        #prefix
        self.rand()
        if self.seed % 5 == 0:
            self.rand()
            domain += self.prefix[self.seed % len(self.prefix)]
            domain += '.'

        #verb
        self.rand()
        domain += self.verbs[self.seed % len(self.verbs)]

        self.rand()
        if self.seed % 10 <= 1:
            domain += '-'

        #adj
        self.rand()
        domain += self.adjs[self.seed % len(self.adjs)]
        
        self.rand()
        if self.seed % 10 <= 1:
            domain += '-'

        #noun
        self.rand()
        domain += self.nouns[self.seed % len(self.nouns)]
        
        #TLD
        self.rand()
        domain += '.' + self.tlds[self.seed % len(self.tlds)]
        
        return domain
    
    def generate_domains(self, nr):
        for d in range(nr):
            print(self.generate_domain())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--time', help="Seconds since January 1, 1970 UTC")
    parser.add_argument("-n", "--nr", help="nr of domains", type=int, default=1000)

    args = parser.parse_args()

    dg = domain_generator(int(args.time))
    dg.generate_domains(int(args.nr))
