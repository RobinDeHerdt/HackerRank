# https://www.hackerrank.com/challenges/acm-icpc-team/problem
from Testing import assertions

# Returns the combined topics of every 2-person team.
def acm_team_combined_topics(topics):
    combined_topics = []
    for i in range(len(topics)):
        for j in range(len(topics)):
            if i == j or j < i:
                continue

            combined_topic_count = 0
            for k in range(len(topics[i])):
                if topics[i][k] == '1' or topics[j][k] == '1':
                    combined_topic_count += 1

            combined_topics.append(combined_topic_count)

    return combined_topics

# Returns the maximum number of topics a 2-person team can know.
def acm_team_max_topics(topics):
    combined_topics = acm_team_combined_topics(topics)
    return max(combined_topics)

# Number of ways to form a 2-person team that knows the maximum number of topics.
def acm_team_max_combination_count(topics):

    combined_topics = acm_team_combined_topics(topics)
    return combined_topics.count(max(combined_topics))

assertions.assert_equals(5, acm_team_max_topics(['10101', '11100', '11010', '00101']))
assertions.assert_equals(2, acm_team_max_combination_count(['10101', '11100', '11010', '00101']))

assertions.assert_equals(5, acm_team_max_topics(['11101', '10101', '11001', '10111', '10000', '01110']))
assertions.assert_equals(6, acm_team_max_combination_count(['11101', '10101', '11001', '10111', '10000', '01110']))
