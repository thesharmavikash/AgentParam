import json
import os

class CostTracker:
    def __init__(self):
        # ... (previous init)
        self.user_focus_level = 100 # 0-100% focus
        self.user_stress_level = 0 # 0-100% stress

    def update_bio_metrics(self, focus, stress):
        """Updates the system with user's physical state to adjust swarm speed."""
        self.user_focus_level = focus
        self.user_stress_level = stress
        
        if stress > 70:
            return "SWARM_MODE: STABILITY_PRIORITY (Slow & Safe)"
        if focus > 80:
            return "SWARM_MODE: SILENT_EXECUTION (Do not disturb)"
        return "SWARM_MODE: STANDARD"

    def analyze_sentiment(self, text: str):
        """Simple keyword-based sentiment analysis to adjust swarm behavior."""
        urgent_keywords = ["fast", "urgent", "now", "immediately", "asap", "deadline"]
        chill_keywords = ["learn", "explain", "how", "why", "curious", "understand"]
        
        text_lower = text.lower()
        if any(k in text_lower for k in urgent_keywords):
            self.user_sentiment = "STRESSED/URGENT"
            self.urgency_level = 2.0
        elif any(k in text_lower for k in chill_keywords):
            self.user_sentiment = "CURIOUS/EDUCATIONAL"
            self.urgency_level = 0.5
        else:
            self.user_sentiment = "NEUTRAL"
            self.urgency_level = 1.0
        
        return self.user_sentiment

    def update(self, response_msg, success=True):
        content = response_msg.content
        agent_name = response_msg.name
        # ... (token calculation)
        
        if agent_name not in self.trust_scores:
            self.trust_scores[agent_name] = 100 # Initial trust
        
        # Adjust trust based on success/failure
        if success:
            self.trust_scores[agent_name] = min(100, self.trust_scores[agent_name] + 1)
        else:
            self.trust_scores[agent_name] = max(0, self.trust_scores[agent_name] - 10)

    def get_best_model(self, task_type):
        """NEW: Token Arbitrage - Simulates choosing the cheapest/fastest model."""
        # In real-world, this would ping an API for live pricing/latency
        return "openai_efficient" if task_type == "simple" else "openai_complex"
        
        # Track Agent KPIs
        if agent_name not in self.agent_stats:
            self.agent_stats[agent_name] = {"calls": 0, "tokens": 0, "cost": 0}
        
        self.agent_stats[agent_name]["calls"] += 1
        self.agent_stats[agent_name]["tokens"] += (in_tokens + out_tokens)
        self.agent_stats[agent_name]["cost"] += (in_tokens * self.input_price) + (out_tokens * self.output_price)

    def save_stats(self, company_name):
        """Persists agent performance data to the company folder."""
        stats_path = f"companies/{company_name}/agent_kpis.json"
        with open(stats_path, "w") as f:
            json.dump(self.agent_stats, f, indent=4)

    def get_report(self):
        cost = (self.total_input_tokens * self.input_price) + (self.total_output_tokens * self.output_price)
        return {
            "input_tokens": self.total_input_tokens,
            "output_tokens": self.total_output_tokens,
            "total_cost_usd": round(cost, 4)
        }

    def is_over_budget(self, limit_usd: float):
        """Checks if the current session has exceeded the dollar limit."""
        current_cost = (self.total_input_tokens * self.input_price) + (self.total_output_tokens * self.output_price)
        return current_cost >= limit_usd

cost_tracker = CostTracker()
