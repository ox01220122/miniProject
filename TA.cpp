#include <iostream>
#include <ctime>
#include <vector>
#include <string>
using namespace std;
int main() {	
	vector <string> save_word = {"egg"};
	string input_word;
	double count_time = 0;
	clock_t startTime = clock();
	int temp;

	cout << save_word.front() << endl;
	while (count_time <= 30000) {
		char change_word = save_word.back().back();
		cout << "���� �ܾ �Է��ϼ��� : ";
		cin >> input_word;
		cout << change_word << endl;
		cout << input_word[input_word.size() - 1] << endl;		
		clock_t endTime = clock();
		count_time = endTime - startTime; //�Է� ���� �� 30�� �ʰ� �� �ݺ��� Ż��

		if (input_word[0] == change_word) {
			save_word.push_back(input_word);
			temp = 2;
		}

		else {
			cout << "Ʋ�Ƚ��ϴ�" << endl;
			temp = 1;
		}
	}


	cout << "�ð��� �ʰ� �Ǿ����ϴ�!" << endl;
	cout << "�Է��� �ܾ��� ������ : " << save_word.size() - temp << "�Դϴ�"; 
	
}