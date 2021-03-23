def solution(bridge_length: int, weight: int, truck_weights: list) -> int:
    time = 0 # 시간 검사
    bridge = [] #브릿지 함수
    weight_monitoring = 0 # weight 모니터링

    while True:
        time += 1 # 시간을 얻자

        size = len(bridge)
        for _ in range(size):
            temp_weight, length = bridge.pop(0)

            if length <= 1:
                weight_monitoring -= temp_weight
                continue
            bridge.append([temp_weight, length-1])

        if truck_weights and weight_monitoring+truck_weights[0] <= weight:
            weight_monitoring += truck_weights[0]
            bridge.append([truck_weights[0], bridge_length])
            truck_weights.pop(0)

        if not truck_weights and not bridge:
            # 기다리는 사람이 없고 카운트가 되지 않으면
            break

    return time