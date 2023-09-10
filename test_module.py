from mean_var_std import calculate


class TestCalculate:

    def test_calculate(self):
        result = {
            'mean': [[3., 4., 5.], [1., 4., 7.], 4.0],
            'variance': [[6., 6., 6.], [0.66666667, 0.66666667, 0.66666667], 6.666666666666667],
            'standard deviation': [[2.44948974, 2.44948974, 2.44948974], [0.81649658, 0.81649658, 0.81649658], 2.581988897471611],
            'max': [[6, 7, 8], [2, 5, 8], 8],
            'min': [[0, 1, 2], [0, 3, 6], 0],
            'sum': [[ 9, 12, 15], [ 3, 12, 21], 36]
            }
        assert print(calculate([0,1,2,3,4,5,6,7,8])) == print(result)