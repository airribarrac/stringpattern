#include <bits/stdc++.h>
using namespace std;

void NaiveSearch(char* str, const char* pat){
	int x = strlen(str);
	int y = strlen(pat);
	int i;
	for(i=0; i<x; i++){
		int j;
		for(j=0; j<y; j++){
			if(str[i+j]!=pat[j]){
				break;
			}
		}
		if(j==y){
			printf("Patrón encontrado en indice: %d\n",i);
		}
	}
}

int main(){
	char txt[] = "AGUINALDOOOO";
	char pat[] = "OOO";
	NaiveSearch(txt,pat);
}