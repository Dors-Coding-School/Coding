#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    for(int w = 0; w < width; w++){
        for(int h = 0; h < height; h++){
            if(image[h][w].rgbtBlue == 0 && image[h][w].rgbtGreen == 0 && image[h][w].rgbtRed == 0){
                image[h][w].rgbtBlue = 127;
                image[h][w].rgbtGreen = 0;
                image[h][w].rgbtRed = 255;
            }
        }
    }
}
