#include <iostream>
#include <string>
#include <ctime>
using namespace std;
int main() {

	srand(time(NULL));
	int com_num = 0, user_num=0;
	const int range_num = 3; //������ ����� �� ������ ���ڸ� �ٲ��ֱ�
	int com_arr[range_num], user_arr[range_num];
	int strike_count=0, ball_count=0;
	
	
	for (int i = 0; i < range_num; i++){//��ǻ�� �������� ���� 
		com_num = (rand() % 9) + 1;
		for (int c : com_arr) {
			if (c == com_num) { i--; continue; }
		}
		com_arr[i] = com_num;
	}

	int repeat=0;
	while (strike_count != range_num) {
		strike_count = 0, ball_count = 0;
		cout << "1~9������ ���� " <<range_num<<"���� �Է��Ͻÿ�(�̿��� ���� : ����) " << endl;
		cin >> user_arr[0] >> user_arr[1] >> user_arr[2];

		for (int i = 0; i < range_num; i++){//strike �˻� 
			if (user_arr[i] <= 0 || user_arr[i] >= 10) { exit(1); } //���� ���� ���ڸ� �Է� �� ����

			if (com_arr[i] == user_arr[i]){	strike_count++;	}
			for (int j = 0; j < range_num; j++) {//ball �˻� 
				if (com_arr[i] == user_arr[j]) { ball_count++; }
			}
		}
		ball_count -= strike_count;
		cout << "strike : " << strike_count << "ball : " << ball_count << endl;
		repeat++;
	}
	cout << repeat << "���� ������ϴ�!" << endl;


	return 0;
}