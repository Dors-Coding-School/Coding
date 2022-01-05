#include "helpers.h"
#include <math.h>
#define MAX_RGB_VALUE 255
#define COLUMN_TO_LEFT -1
#define COLUMN_TO_RIGHT 1

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{

    for (int i = 0; i < width; i++)
    {
        for (int j = 0; j < height; j++)
        {
            // averages the color intensity and then applies the same value to all the colors to get gray
            int rgbGray = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);

            image[i][j].rgbtBlue = rgbGray;
            image[i][j].rgbtGreen = rgbGray;
            image[i][j].rgbtRed = rgbGray;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            int sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            int sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);

            image[i][j].rgbtRed = fmin(MAX_RGB_VALUE, sepiaRed);
            image[i][j].rgbtBlue = fmin(MAX_RGB_VALUE, sepiaBlue);
            image[i][j].rgbtGreen = fmin(MAX_RGB_VALUE, sepiaGreen);
        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
     // Temporary storage
    RGBTRIPLE temp;

    // Iterate over every row of the image
    for (int i = 0; i < height; i++)
    {
        // Iterate over every column that are less than width / 2
        for (int j = 0; j < width / 2; j++)
        {
            // Swap pixels on horizontally opposite sides
            temp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }
    return;
}


// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE returnImage[height][width];
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            returnImage[h][w] = image[h][w];
        }
    }
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
           
            int blueAver = 0;
            int greenAver = 0;
            int redAver = 0;
            double count = 0;
            for (int offset_x = ROW_ABOVE; offset_x <= ROW_BELOW; offset_x++)
            {
                 for (int offset_y =COLUMN_TO_LEFT ; offset_y < COLUMN_TO_RIGHT; offset_y++)
                 {
                     
                 }
            }
    
            }
            image[h][w].rgbtBlue = round(blueAver/count);
            image[h][w].rgbtGreen = round(greenAver/count);
            image[h][w].rgbtRed = round(redAver/count);
           
        }
    }
    return;
   
}