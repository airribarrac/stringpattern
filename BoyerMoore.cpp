#include <bits/stdc++.h>
#define SIZE_ALPHABET 256 
using namespace std;

void preprocessing(char* pat, int array[]){
	int m = strlen(pat);
	for(int i=0; i<SIZE_ALPHABET; i++){
		array[i] = -1;
	}
	for(int i=0; i<m; i++){
		array[(int) pat[i]] = i;
	}

}


void BoyerMoore(char *str, char *pat){
	int n = strlen(str);
	int m = strlen(pat);
	int badchar[256];
	preprocessing(pat,badchar);
	int i=0;
	int j;
	while(i <= (n-m)){
		j = m-1;
		while(j >= 0 && pat[j]==str[i+j]){
			j--;
		}
		if(j < 0){
			printf("Patron encontrado en %d\n",i);
			i += (i+m < n)? m-badchar[str[i+m]] : 1; 
		}
		else{
			i += max(1, j - badchar[str[i+j]]);
		}
	}
} 


int main(){
	char txt[] = "AGUINALDOOOO";
	char pat[] = "OOO";
	BoyerMoore(txt,pat);
}