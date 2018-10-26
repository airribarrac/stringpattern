#include <bits/stdc++.h>
using namespace std;

class PatternSearcher{
private:
	char *T,*P;
	int n,m;
public:
	PatternSearcher(string text,string pat){
		T = new char[text.size()+1];
		strcpy(T,text.c_str());
		n = text.size();
		P = new char[pat.size()+1];
		strcpy(P,pat.c_str());
		m = pat.size();
	}
	void setPattern(string pat){
		delete[] P;
		P = new char[pat.size()+1];
		strcpy(P,pat.c_str());
		m = pat.size();
	}

	void NaiveSearch(){
		char* str = T, *pat= P;
		int x = n;
		int y = m;
		int i;
		for(i=0; i<x; i++){
			int j;
			for(j=0; j<y; j++){
				if(str[i+j]!=pat[j]){
					break;
				}
			}
			if(j==y){
				//do something
				//printf("Patrón encontrado en indice: %d\n",i);
			}
		}
	}

	void BMpreprocessing(int array[]){
		for(int i=0; i<256; i++){
			array[i] = -1;
		}
		for(int i=0; i<m; i++){
			array[(int) P[i]] = i;
		}
	}

	void BoyerMoore(){
		char *str = T, *pat =P;
		int badchar[256];
		BMpreprocessing(badchar);
		int i=0;
		int j;
		while(i <= (n-m)){
			j = m-1;
			while(j >= 0 && pat[j]==str[i+j]){
				j--;
			}
			if(j < 0){
				//do something
				//printf("Patron encontrado en %d\n",i);
				i += (i+m < n)? m-badchar[str[i+m]] : 1; 
			}
			else{
				i += max(1, j - badchar[str[i+j]]);
			}
		}
	} 
	void KMPpreprocessing(int lps[]){
		int i=0,j=-1;
		lps[0]=-1;
		while(i<m){
			while(j>=0 && P[i]!=P[j]){
				j=lps[j];
			}
			i++;
			j++;
			lps[i]=j;
		}
	}

	void KMPsearch(){
		int i=0,j=0;
		int lps[m+1];
		KMPpreprocessing(lps);
		while(i<n){
			while(j>=0 && T[i]!=P[j]){
				j=lps[j];
			}
			i++;
			j++;
			if(j==m){
				//do something
				//printf("Patrón encontrado en indice: %d\n",i-j);
				j=lps[j];
			}
		}
	}
};

int main(int argc,char *argv[]){
	ifstream texto,patrones;
	int iters = atoi(argv[3]);
	texto.open(argv[1]);
	patrones.open(argv[2]);
	string leido,patron;
	getline(texto,leido,(char)texto.eof());
	getline(patrones,patron,(char)patrones.eof());
	PatternSearcher(leido,patron);
	for(int i=0;i<iters;i++){
		clock_t start = clock();
		PatternSearcher.KMPsearch();
		cout<<((double)(clock()-start)*1000/CLOCKS_PER_SEC)<<endl;
		
		start = clock();
		PatternSearcher.BoyerMoore();
		cout<<((double)(clock()-start)*1000/CLOCKS_PER_SEC)<<endl;

		start = clock();
		PatternSearcher.NaiveSearch();
		cout<<((double)(clock()-start)*1000/CLOCKS_PER_SEC)<<endl;
	}
}	