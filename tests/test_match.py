from services.match_service import MatchService

match = MatchService()

print(match.score("ASPIRINA", "ASPIRINA"))
print(match.score("ASPIRINA", "ASPIRINA ADVANCE"))
print(match.score("PROXEGO", "PASTA DE LASSAR"))