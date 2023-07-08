class CommentsRepository:
    def __init__(self):
        self.comments = [
            {"id": 1, "content": "I'm first user", "category": "positive"}
        ]

    def get_all(self):
        return self.comments

    def get_one(self, comment_id):
        for comment in self.comments:
            if comment["id"] == comment_id:
                return comment
        return None

    def save(self, comment):
        if "id" not in comment or not comment["id"]:
            comment["id"] = self.get_next_id()
        self.comments.append(comment)
        return comment

    def get_next_id(self):
        return len(self.comments) + 1
