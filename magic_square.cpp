#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

void input_odd_num(int* input_odd_num) {//Ȧ���� �Է¹޴´� 
	while (*input_odd_num == 0) { 
		cout << "������ ��, Ȥ�� ���� ���� �ڿ����� �Է��� �ּ���(Ȧ�� �Է�) : ";
		cin >> *input_odd_num;
		if (*input_odd_num % 2 == 0 || *input_odd_num <= 0) {
			cout << "0 �̻��� Ȧ���� �Է��ϼ���" << endl;
			*input_odd_num = 0;
		}
	}
}

void print_magic_square(int input_number,vector<vector<int>> magic_square) {
	for (int j = 0; j < input_number; j++) {//������ ���
		for (int k = 0; k < input_number; k++) {
			cout << magic_square[j][k] << " ";
		}
		cout << endl;
	}
}


int main() {
	int input_number = 0;
	input_odd_num(&input_number); // Ȧ�� �Է¹ޱ� 
	

	vector<vector<int>> magic_square(input_number, vector<int>(input_number, 0));
	int row = 0;
	int col = floor(input_number / 2.0);
	magic_square[row][col] = 1;  //ù��° �� ��� 1�� �־��ְ� ����
	
	for (int i = 2; i <= pow(input_number, 2); i++){//2���� ���� �־��ֱ�

		if (col + 1 == input_number && row - 1 < 0){//��� ���� ������ ����� ���
			row = input_number - 1;
			col = 0;

			if (magic_square[row][col] != 0){
				row = 1;
				col = input_number - 1;
				magic_square[row][col] = i;
			}
			else { magic_square[row][col] = i;	continue; }
		}

		else if (col + 1 == input_number){//���� ������ ����� ��� 
			row -= 1;
			col = 0;
		}

		else if (row - 1 < 0){//���� ������ ����� ���
			row = input_number - 1;
			col += 1;
		}

		else if (magic_square[row - 1][col + 1] != 0){//ä���������� ���� �̹� ���� ���� ���
			row += 1;
		}

		else {//������ ��ĭ ,���� ��ĭ ���� �� �־��ֱ� 
			row -= 1;
			col += 1;
		}
		magic_square[row][col] = i;
	}
		
	print_magic_square(input_number, magic_square);

}