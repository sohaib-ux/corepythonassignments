def positive_feedback_percentage(ratings):
    if not ratings:
        return "No feedback available"
    
    positive_ratings = [rating for rating in ratings if rating >= 4]
    return (len(positive_ratings) / len(ratings)) * 100

ratings = [5, 4, 3, 5, 2, 4, 1, 5]
positive_percentage = positive_feedback_percentage(ratings)
print(f"{positive_percentage}%")
