import random

class Resource:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.locked_by = []

    def request(self, agent_id: str) -> bool:
        if len(self.locked_by) < self.capacity:
            self.locked_by.append(agent_id)
            return True
        return False

    def release(self, agent_id: str):
        if agent_id in self.locked_by:
            self.locked_by.remove(agent_id)

class Patient:
    def __init__(self, patient_id: int):
        self.patient_id = patient_id
        self.symptoms = random.sample(
            [
                "fever", "cough", "fatigue", "headache", "chest pain",
                "numbness", "blurred vision", "slurred speech", "dizziness"
            ],
            3
        )
        self.true_condition = random.choice(["flu", "stroke", "heart_attack", "migraine"])
