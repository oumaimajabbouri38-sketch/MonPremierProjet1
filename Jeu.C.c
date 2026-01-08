#include <stdio.h>

int main()
{
    int secret = 7;
     int choix;
   printf("Entrez  le nombre (entre 1 a 10): ");
   scanf("%d", &choix);
   if (choix == secret){
   printf(" Bravo!  valide \n");
   } else {
   printf("Rate! invalide %d.\n", secret);
   }
   
   return 0;
}