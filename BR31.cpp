#include <iostream>
#include <ctime>
using namespace std;
void F_print(int* num_counter, bool* bool_end, int creat_num , int range) { //user, ��ǻ�� ������� & ���� ī��Ʈ 
	for (int j = *num_counter + 1; j <= *num_counter + creat_num; j++) {
		cout << j << endl;
		if (j == range) {
			*bool_end = 1; 
			break;
		}
	}
	*num_counter += creat_num;
}

void F_input_user(int *input_num) {//user ���� �Է¹ޱ� 
	cout << "������ �Է��ϼ���";
	cin >> *input_num;
	cout << *input_num << "�� �Է��ϼ̽��ϴ�" << endl;
}

void F_input_com(int *com_num) {//��ǻ�� ���� ��ȣ ���� 
	*com_num = (rand() % 3) + 1; 
	cout << "��ǻ�Ͱ� �θ� ���� : " << *com_num << endl;
}

int main() {
	srand(time(NULL));
	int input_num = 0, com_num = 0, num_counter = 0;
	bool input_end=0, com_end=0;

	while (true){
		if (com_end) {
			cout << "����ڰ� �̰���ϴ�!";
			exit(1);
		}
		else if (input_end) {
			cout << "��ǻ�Ͱ� �̰���ϴ�!";
			exit(1);
		}

		F_input_user(&input_num);

		if (input_num <= 3 && input_num > 0){
			F_print(&num_counter, &input_end, input_num, 31);
		}
		else {
			cout << "������ ������ϴ�. �ٽ��Է��ϼ���" << endl;
			continue;
		}
		if (input_end) { continue; } 
		F_input_com(&com_num);
		F_print(&num_counter, &com_end, com_num,31);
	}
	return 0;
}