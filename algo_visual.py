import pygame
import random
import math
import time


pygame.init()

#Diafora Xrwmata - Fonts pou xrhsimopoioyntai kat'olh thn diarkeia ths ergasias
class DrawInformation:      #backround and font colour
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 0, 200
    RED = 0, 255, 255
    BACKGROUND_COLOR = BLACK

    GRADIENTS = [           #rectangle colours
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    FONT = pygame.font.SysFont('verdana', 26)           #fonts
    LARGE_FONT = pygame.font.SysFont('verdana', 40)

    SIDE_PAD = 100          #black space at the sides and top
    TOP_PAD = 150

    def __init__(self, width, height, lst):           #inisilasation of list and window setup and name of window
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Απεικόνιση Αλγορίθμων Ταξινόμησης ")
        self.set_list(lst)

    def set_list(self, lst):            #method for attributes related to the list
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2

# Xarakthres pou emfanizontai sthn othonh gia oles tis leitourgies (Algorithmoi taxinomishs, algorithmoi anazhtishs se oles tous tis morfes, mazi me "if" gia to pote na emfanizontai
# ASC = ASCENIDNG, DES = DESCENDING
def draw(draw_info, algo_name, ascending,flag,sorting_algorithm,flag2,current_search_algo,current_search_algo_name):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    if flag2== False:
        title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Αύξουσα' if ascending else 'Φθίνουσα'}", 1,
                                            draw_info.RED)
        draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 5))

        controls = draw_info.FONT.render("R - Επαναφορά | SPACE - Εκκίνηση Ταξινόμησης | A - Αύξουσα | D - Φθίνουσα | Q - Εμφάνιση κώδικα | L - Αλγ.Αναζήτησης", 1,
                                         draw_info.WHITE)
        draw_info.window.blit(controls, (draw_info.width / 2 - controls.get_width() / 2, 45))

        sorting = draw_info.FONT.render(
            "I - Insertion Sort | B - Bubble Sort | S - Selection Sort | H - Shell Sort | C - Cocktail Sort", 1,
            draw_info.WHITE)
        draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 75))
    else:
        title = draw_info.LARGE_FONT.render(f"{current_search_algo_name} ", 1,
                                            draw_info.RED)
        draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 5))

        sorting = draw_info.FONT.render(
            "1 - Binary Search | 2 - Linear Search | 3 - Jump Search | 4 - Exponential Search", 1,
            draw_info.WHITE)
        draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 75))

        # BINARY SEARCH
        if current_search_algo == "binary_search" :
            sorting = draw_info.FONT.render(
                "def binary_search(arr, low, high, x):", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 150))
            sorting = draw_info.FONT.render(
                "if high >= low:", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 200))
            sorting = draw_info.FONT.render(
                "mid = (high + low) // 2", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 250))
            sorting = draw_info.FONT.render(
                "if arr[mid] == x:", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 300))
            sorting = draw_info.FONT.render(
                "return mid", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 350))
            sorting = draw_info.FONT.render(
                "elif arr[mid] > x:", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 400))
            sorting = draw_info.FONT.render(
                "return binary_search(arr, low, mid - 1, x)", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 450))
            sorting = draw_info.FONT.render(
                "else:", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 500))
            sorting = draw_info.FONT.render(
                "return binary_search(arr, mid + 1, high, x)", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 550))
            sorting = draw_info.FONT.render(
                "else:", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 600))
            sorting = draw_info.FONT.render(
                "return -1", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 650))

#LINEAR SEARCH
        elif current_search_algo == "linear_search" :
            sorting = draw_info.FONT.render(
                "def search(arr, x):", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 150))
            sorting = draw_info.FONT.render(
                "for i in range(len(arr)):", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 200))
            sorting = draw_info.FONT.render(
                "if arr[i] == x:", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 250))
            sorting = draw_info.FONT.render(
                "return i", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 300))
            sorting = draw_info.FONT.render(
                "return -1", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 350))

#JUMP SEARCH
        elif current_search_algo == "jump_search" :
                sorting = draw_info.FONT.render(
                    "def jumpSearch( arr , x , n ):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 150))
                sorting = draw_info.FONT.render(
                    "step = math.sqrt(n)", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 200))
                sorting = draw_info.FONT.render(
                    "prev = 0", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 250))
                sorting = draw_info.FONT.render(
                    "while arr[int(min(step, n)-1)] < x:", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 300))
                sorting = draw_info.FONT.render(
                    "prev = step", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 350))
                sorting = draw_info.FONT.render(
                    "step += math.sqrt(n)", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 400))
                sorting = draw_info.FONT.render(
                    "if prev >= n:", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 450))
                sorting = draw_info.FONT.render(
                    "return -1", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 500))
                sorting = draw_info.FONT.render(
                    "while arr[int(prev)] < x:", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 550))
                sorting = draw_info.FONT.render(
                    "prev += 1", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 600))
                sorting = draw_info.FONT.render(
                    "if prev == min(step, n):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 150))
                sorting = draw_info.FONT.render(
                    "return -1", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 200))
                sorting = draw_info.FONT.render(
                    "if arr[int(prev)] == x:", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 250))
                sorting = draw_info.FONT.render(
                    "return prev", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 300))
                sorting = draw_info.FONT.render(
                    "return -1", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 350))

#EXPONENTIAL SEARCH
        elif current_search_algo == "exponential_search" :
                sorting = draw_info.FONT.render(
                    "def binarySearch( arr, l, r, x):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 150))
                sorting = draw_info.FONT.render(
                    "if r >= l:", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 200))
                sorting = draw_info.FONT.render(
                    "mid = l + ( r-l ) // 2", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 250))
                sorting = draw_info.FONT.render(
                    "if arr[mid] == x:", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 300))
                sorting = draw_info.FONT.render(
                    "return mid", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 350))
                sorting = draw_info.FONT.render(
                    "if arr[mid] > x:", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 400))
                sorting = draw_info.FONT.render(
                    "return binarySearch(arr, l,mid - 1, x)", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 450))
                sorting = draw_info.FONT.render(
                    "return binarySearch(arr, mid + 1, r, x)", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 500))
                sorting = draw_info.FONT.render(
                    "return -1", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 550))
                sorting = draw_info.FONT.render(
                    "def exponentialSearch(arr, n, x):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 600))
                sorting = draw_info.FONT.render(
                    "if arr[0] == x:", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 150))
                sorting = draw_info.FONT.render(
                    "return 0", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 200))
                sorting = draw_info.FONT.render(
                    "i = 1", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 250))
                sorting = draw_info.FONT.render(
                    "while i < n and arr[i] <= x:", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 300))
                sorting = draw_info.FONT.render(
                    "i = i * 2", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 350))
                sorting = draw_info.FONT.render(
                    "return binarySearch( arr, i // 2,min(i, n-1), x)", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.4 - sorting.get_width() / 2, 400))


#BUBBLESORT ASC
    if flag == True:
        if sorting_algorithm == bubble_sort and ascending== True:
            sorting = draw_info.FONT.render(
                "def bubbleSort(arr):", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 150))
            sorting = draw_info.FONT.render(
                "n = len(arr)", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 200))
            sorting = draw_info.FONT.render(
                "for i in range(n-1):", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 250))
            sorting = draw_info.FONT.render(
                "for j in range(0, n-i-1):", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 300))
            sorting = draw_info.FONT.render(
                "if arr[j] > arr[j + 1] :", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 350))
            sorting = draw_info.FONT.render(
                "arr[j], arr[j + 1] = arr[j + 1], arr[j]", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 400))

#BUBBLESORT DES
        elif sorting_algorithm == bubble_sort and ascending== False:
            sorting = draw_info.FONT.render(
                "def bubbleSort(arr):", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 150))
            sorting = draw_info.FONT.render(
                "n = len(arr)", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 200))
            sorting = draw_info.FONT.render(
                "for i in range(n-1):", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 250))
            sorting = draw_info.FONT.render(
                "for j in range(0, n-i-1):", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 300))
            sorting = draw_info.FONT.render(
                "if arr[j] < arr[j + 1] :", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 350))
            sorting = draw_info.FONT.render(
                "arr[j], arr[j + 1] = arr[j + 1], arr[j]", 1,
                draw_info.WHITE)
            draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 400))


#SELECTIONSORT ASC
        elif sorting_algorithm == selection_sort and ascending == True:
                sorting = draw_info.FONT.render(
                    "def selectionSort(arr):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 150))
                sorting = draw_info.FONT.render(
                    "for i in range(len(arr)):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 200))
                sorting = draw_info.FONT.render(
                    "min_idx = i", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 250))
                sorting = draw_info.FONT.render(
                    "for j in range(i+1, len(arr)):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 300))
                sorting = draw_info.FONT.render(
                    "if arr[min_idx] > arr[j]:", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 350))
                sorting = draw_info.FONT.render(
                    "min_idx = j", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 400))
                sorting = draw_info.FONT.render(
                    "arr[i], arr[min_idx] = arr[min_idx], arr[i]", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 450))

#SELECTIONSORT DES

        elif sorting_algorithm == selection_sort and ascending == False:
                sorting = draw_info.FONT.render(
                    "def selectionSort(arr):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 150))
                sorting = draw_info.FONT.render(
                    "for i in range(len(arr)):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 200))
                sorting = draw_info.FONT.render(
                    "min_idx = i", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 250))
                sorting = draw_info.FONT.render(
                    "for j in range(i+1, len(arr)):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 300))
                sorting = draw_info.FONT.render(
                    "if arr[min_idx] < arr[j]:", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 350))
                sorting = draw_info.FONT.render(
                    "min_idx = j", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 400))
                sorting = draw_info.FONT.render(
                    "arr[i], arr[min_idx] = arr[min_idx], arr[i]", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 450))

#INSERTIONSORT ASC
        elif sorting_algorithm == insertion_sort and ascending == True:
                sorting = draw_info.FONT.render(
                    "def insertionSort(arr):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 150))
                sorting = draw_info.FONT.render(
                    "for i in range(1, len(arr)):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 200))
                sorting = draw_info.FONT.render(
                    "key = arr[i]", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 250))
                sorting = draw_info.FONT.render(
                    "j = i-1", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 300))
                sorting = draw_info.FONT.render(
                    "while j >=0 and key < arr[j] :", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 350))
                sorting = draw_info.FONT.render(
                    "arr[j+1] = arr[j]", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 400))
                sorting = draw_info.FONT.render(
                    "j -= 1", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 450))
                sorting = draw_info.FONT.render(
                    "arr[j+1] = key", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 500))

#INSERTIONSORT DES
        elif sorting_algorithm == insertion_sort and ascending == False:
                sorting = draw_info.FONT.render(
                    "def insertionSort(arr):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 150))
                sorting = draw_info.FONT.render(
                    "for i in range(1, len(arr)):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 200))
                sorting = draw_info.FONT.render(
                    "key = arr[i]", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 250))
                sorting = draw_info.FONT.render(
                    "j = i-1", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 300))
                sorting = draw_info.FONT.render(
                    "while j >=0 and key > arr[j] :", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 350))
                sorting = draw_info.FONT.render(
                    "arr[j+1] = arr[j]", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 400))
                sorting = draw_info.FONT.render(
                    "j -= 1", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 450))
                sorting = draw_info.FONT.render(
                    "arr[j+1] = key", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 500))

#SHELLSORT ASC
        elif sorting_algorithm == shellSort and ascending == True:
                sorting = draw_info.FONT.render(
                    "def shellSort(arr):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 150))
                sorting = draw_info.FONT.render(
                    "n = len(arr)", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 200))
                sorting = draw_info.FONT.render(
                    "gap = n/2", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 250))
                sorting = draw_info.FONT.render(
                    "while gap > 0:", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 300))
                sorting = draw_info.FONT.render(
                    "for i in range(gap,n):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 350))
                sorting = draw_info.FONT.render(
                    "temp = arr[i]", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 400))
                sorting = draw_info.FONT.render(
                    "j = i", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 450))
                sorting = draw_info.FONT.render(
                    "while  j >= gap and arr[j-gap] >temp:", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 500))
                sorting = draw_info.FONT.render(
                    "arr[j] = arr[j-gap]", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 550))
                sorting = draw_info.FONT.render(
                    "j -= gap", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 600))
                sorting = draw_info.FONT.render(
                    "arr[j] = temp", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 650))
                sorting = draw_info.FONT.render(
                    "gap /= 2", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 700))

#SHELLSORT DES
        elif sorting_algorithm == shellSort and ascending == False:
                sorting = draw_info.FONT.render(
                    "def shellSort(arr):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 150))
                sorting = draw_info.FONT.render(
                    "n = len(arr)", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 200))
                sorting = draw_info.FONT.render(
                    "gap = n/2", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 250))
                sorting = draw_info.FONT.render(
                    "while gap > 0:", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 300))
                sorting = draw_info.FONT.render(
                    "for i in range(gap,n):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 350))
                sorting = draw_info.FONT.render(
                    "temp = arr[i]", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 400))
                sorting = draw_info.FONT.render(
                    "j = i", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 450))
                sorting = draw_info.FONT.render(
                    "while  j >= gap and arr[j-gap] <temp:", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 500))
                sorting = draw_info.FONT.render(
                    "arr[j] = arr[j-gap]", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 550))
                sorting = draw_info.FONT.render(
                    "j -= gap", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 600))
                sorting = draw_info.FONT.render(
                    "arr[j] = temp", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 650))
                sorting = draw_info.FONT.render(
                    "gap /= 2", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 700))

#COCKTAILSORT ASC
        elif sorting_algorithm == cocktailSort and ascending == True:
                sorting = draw_info.FONT.render(
                    "def cocktailSort(arr):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 150))
                sorting = draw_info.FONT.render(
                    "n = len(arr)", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 200))
                sorting = draw_info.FONT.render(
                    "swapped = True", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 250))
                sorting = draw_info.FONT.render(
                    "start = 0", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 300))
                sorting = draw_info.FONT.render(
                    "end = n-1", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 350))
                sorting = draw_info.FONT.render(
                    "while (swapped==True):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 400))
                sorting = draw_info.FONT.render(
                    "swapped = False", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 450))
                sorting = draw_info.FONT.render(
                    "for i in range (start, end):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 500))
                sorting = draw_info.FONT.render(
                    "if (arr[i] > arr[i+1]) :", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 550))
                sorting = draw_info.FONT.render(
                    "arr[i], arr[i+1]= arr[i+1], arr[i]", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 600))
                sorting = draw_info.FONT.render(
                    "swapped=True", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 150))
                sorting = draw_info.FONT.render(
                    "if (swapped==False):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 200))
                sorting = draw_info.FONT.render(
                    "break", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 250))
                sorting = draw_info.FONT.render(
                    "swapped = False", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 300))
                sorting = draw_info.FONT.render(
                    "end = end-1", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 350))
                sorting = draw_info.FONT.render(
                    "for i in range(end-1, start-1,-1):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 400))
                sorting = draw_info.FONT.render(
                    "if (a[i] > a[i+1]):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 450))
                sorting = draw_info.FONT.render(
                    "a[i], a[i+1] = a[i+1], a[i]", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 500))
                sorting = draw_info.FONT.render(
                    "swapped = True", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 550))
                sorting = draw_info.FONT.render(
                    "start = start+1", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 600))

#COCKTAILSORT DES
        elif sorting_algorithm == cocktailSort and ascending == False:
                sorting = draw_info.FONT.render(
                    "def cocktailSort(arr):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 150))
                sorting = draw_info.FONT.render(
                    "n = len(arr)", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 200))
                sorting = draw_info.FONT.render(
                    "swapped = True", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 250))
                sorting = draw_info.FONT.render(
                    "start = 0", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 300))
                sorting = draw_info.FONT.render(
                    "end = n-1", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 350))
                sorting = draw_info.FONT.render(
                    "while (swapped==True):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 400))
                sorting = draw_info.FONT.render(
                    "swapped = False", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 450))
                sorting = draw_info.FONT.render(
                    "for i in range (start, end):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 500))
                sorting = draw_info.FONT.render(
                    "if (arr[i] < arr[i+1]) :", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 550))
                sorting = draw_info.FONT.render(
                    "arr[i], arr[i+1]= arr[i+1], arr[i]", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 3 - sorting.get_width() / 2, 600))
                sorting = draw_info.FONT.render(
                    "swapped=True", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 150))
                sorting = draw_info.FONT.render(
                    "if (swapped==False):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 200))
                sorting = draw_info.FONT.render(
                    "break", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 250))
                sorting = draw_info.FONT.render(
                    "swapped = False", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 300))
                sorting = draw_info.FONT.render(
                    "end = end-1", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 350))
                sorting = draw_info.FONT.render(
                    "for i in range(end-1, start-1,-1):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 400))
                sorting = draw_info.FONT.render(
                    "if (a[i] < a[i+1]):", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 450))
                sorting = draw_info.FONT.render(
                    "a[i], a[i+1] = a[i+1], a[i]", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 500))
                sorting = draw_info.FONT.render(
                    "swapped = True", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 550))
                sorting = draw_info.FONT.render(
                    "start = start+1", 1,
                    draw_info.WHITE)
                draw_info.window.blit(sorting, (draw_info.width / 1.5 - sorting.get_width() / 2, 600))


    if flag == False:
        if flag2 == False:
            draw_list(draw_info)

    pygame.display.update()


def draw_list(draw_info, color_positions={}, clear_bg=False):       #draws the list on screen
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD // 2, draw_info.TOP_PAD,
                      draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        color = draw_info.GRADIENTS[i % 3]

        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))

    if clear_bg:
        pygame.display.update()

# Enarjh diatypwshs algorithmwn gia tajinomhsh
def generate_starting_list(n, min_val, max_val):           #generates starting list
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst


# SELECTION SORT
def selection_sort(draw_info, ascending=True):
    lst = draw_info.lst

    if (ascending == True):
        for i in range(len(lst)):
            min_idx = i
            for j in range(i + 1, len(lst)):
                if lst[min_idx] > lst[j]:
                    min_idx = j
                    draw_list(draw_info, {i: draw_info.GREEN, min_idx: draw_info.RED}, True)
                    yield True
            lst[i], lst[min_idx] = lst[min_idx], lst[i]
            draw_list(draw_info, {i: draw_info.GREEN, min_idx: draw_info.RED}, True)
            yield True
            time.sleep(0.0)
            draw_list(draw_info, {i: draw_info.GREEN, min_idx: draw_info.RED}, True)
            yield True

    else:
        for i in range(len(lst)):
            max_idx = i
            for j in range(i + 1, len(lst)):
                if lst[max_idx] < lst[j]:
                    max_idx = j
                    draw_list(draw_info, {i: draw_info.GREEN, max_idx: draw_info.RED}, True)
                    yield True
            lst[i], lst[max_idx] = lst[max_idx], lst[i]
            draw_list(draw_info, {i: draw_info.GREEN, max_idx: draw_info.RED}, True)
            yield True
            time.sleep(0.0)
            draw_list(draw_info, {i: draw_info.GREEN, max_idx: draw_info.RED}, True)

            yield True

    return lst


# BUBBLESORT
def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                yield True

    return lst


# INSERTION SORT
def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(1, len(lst)):
        current = lst[i]

        while True:
            ascending_sort = i > 0 and lst[i - 1] > current and ascending
            descending_sort = i > 0 and lst[i - 1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = current
            draw_list(draw_info, {i - 1: draw_info.GREEN, i: draw_info.RED}, True)
            yield True

    return lst




# SHELLSORT
def shellSort(draw_info, ascending=True):
    lst = draw_info.lst
    n = len(lst)
    gap = n / 2
    if (ascending == True):
        while gap > 0:

            for i in range(int(gap), n):
                temp = lst[i]
                j = i
                while j >= int(gap) and lst[j - int(gap)] > temp:
                    lst[j] = lst[j - int(gap)]
                    j -= int(gap)
                    draw_list(draw_info, {i: draw_info.GREEN, j: draw_info.RED}, True)
                    yield True
                lst[j] = temp
            draw_list(draw_info, {i: draw_info.GREEN, j : draw_info.RED}, True)
            yield True
            gap /= 2
            time.sleep(0.)
            draw_list(draw_info, {i : draw_info.GREEN, j: draw_info.RED}, True)
            yield True
        return lst
    else :
        while gap > 0:

            for i in range(int(gap), n):
                temp = lst[i]
                j = i
                while j >= int(gap) and lst[j - int(gap)] < temp:
                    lst[j] = lst[j - int(gap)]
                    j -= int(gap)
                    draw_list(draw_info, {i: draw_info.GREEN, j: draw_info.RED}, True)
                    yield True
                lst[j] = temp
            draw_list(draw_info, {i: draw_info.GREEN, j: draw_info.RED}, True)
            yield True
            gap /= 2
            time.sleep(0.)
            draw_list(draw_info, {i: draw_info.GREEN, j: draw_info.RED}, True)
            yield True
        return lst

#COCKTAIL SORT

def cocktailSort(draw_info, ascending=True):
    lst = draw_info.lst
    n = len(lst)
    swapped = True
    start = 0
    end = n - 1
    if (ascending == True):
        while (swapped == True):
            swapped = False
            for i in range(start, end):
                if (lst[i] > lst[i + 1]):
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    swapped = True
            draw_list(draw_info, {i: draw_info.GREEN, i + 1: draw_info.RED}, True)
            yield True
            time.sleep(0.)
            draw_list(draw_info, {i: draw_info.GREEN, i + 1: draw_info.RED}, True)
            yield True
            if (swapped == False):
                break
            swapped = False
            end = end - 1
            for i in range(end - 1, start - 1, -1):
                if (lst[i] > lst[i + 1]):
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    swapped = True
            draw_list(draw_info, {i: draw_info.GREEN, i + 1: draw_info.RED}, True)
            yield True
            start = start + 1
            time.sleep(0.1)
            draw_list(draw_info, {i: draw_info.GREEN, i+1: draw_info.RED}, True)
            yield True
        return lst
    else:
        while (swapped == True):
            swapped = False
            for i in range(start, end):
                if (lst[i] < lst[i + 1]):
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    swapped = True
            draw_list(draw_info, {i: draw_info.GREEN, i + 1: draw_info.RED}, True)
            yield True
            time.sleep(0.)
            draw_list(draw_info, {i: draw_info.GREEN, i + 1: draw_info.RED}, True)
            yield True
            if (swapped == False):
                break
            swapped = False
            end = end - 1
            for i in range(end - 1, start - 1, -1):
                if (lst[i] < lst[i + 1]):
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    swapped = True
            draw_list(draw_info, {i: draw_info.GREEN, i + 1: draw_info.RED}, True)
            yield True
            start = start + 1
            time.sleep(0.1)
            draw_list(draw_info, {i: draw_info.GREEN, i+1: draw_info.RED}, True)
            yield True
        return lst


#Main synarthsh, edw periexontai plhrofories gia to megethos tou parathyrou tou pygame, epishs kallountai oi def.

def main():
    flag = False
    flag2 = False
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(1650, 750, lst)
    sorting = False
    ascending = True

    current_search_algo = "binary_search"
    current_search_algo_name ="Binary Search"


    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None

    while run:
        clock.tick(60)

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algo_name, ascending,flag,sorting_algorithm,flag2,current_search_algo,current_search_algo_name)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
                flag= False
                flag2= False
                current_search_algo = " "
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            elif event.key == pygame.K_q and sorting == False:
                flag = True
            elif event.key == pygame.K_l and sorting == False:
                flag2 = True
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            elif event.key == pygame.K_i and not sorting:
                sorting_algorithm = insertion_sort
                sorting_algo_name = "Insertion Sort"
            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = bubble_sort
                sorting_algo_name = "Bubble Sort"
            elif event.key == pygame.K_s and not sorting:
                sorting_algorithm = selection_sort
                sorting_algo_name = "Selection Sort"
            elif event.key == pygame.K_h and not sorting:
                sorting_algorithm = shellSort
                sorting_algo_name = "Shell Sort"
            elif event.key == pygame.K_c and not sorting:
                sorting_algorithm = cocktailSort
                sorting_algo_name = "Cocktail Sort"
            elif event.key == pygame.K_1 and not sorting:
                current_search_algo = "binary_search"
                current_search_algo_name = "Binary Seach"
            elif event.key == pygame.K_2 and not sorting:
                current_search_algo = "linear_search"
                current_search_algo_name = "Linear Search"
            elif event.key == pygame.K_3 and not sorting:
                current_search_algo = "jump_search"
                current_search_algo_name = "Jump Search"
            elif event.key == pygame.K_4 and not sorting:
                current_search_algo_name = "Exponential Search"
                current_search_algo = "exponential_search"


    pygame.quit()


if __name__ == "__main__":
    main()
