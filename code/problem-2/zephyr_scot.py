def solve(envelopes):
    maxEnvelopes = 1
    for I in range(1, len(envelopes)):
        for j in range(i):
            if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                maxEnvelopes = max(maxEnvelopes, solve(envelopes[j:i+1]) + 1)
        maxEnvelopes = max(maxEnvelopes, solve(envelopes[i:i+1]) + 1)
    return maxEnvelopes
