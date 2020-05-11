## 1. Introduction ##

mean_new = houses_per_year['Mean Price'].mean()
mean_original = houses['SalePrice'].mean()
difference = mean_original-mean_new

## 2. Different Weights ##

houses_per_year['sum_per_year'] = houses_per_year['Mean Price']*houses_per_year['Houses Sold']
all_sums_together = houses_per_year['sum_per_year'].sum()
total_n_houses = houses_per_year['Houses Sold'].sum()
weighted_mean = all_sums_together/total_n_houses
mean_original = houses['SalePrice'].mean()
difference = round(mean_original,10)-round(weighted_mean,10)

## 3. The Weighted Mean ##

def weighted_mean(mean_value,weight_value):
    sum_value = []
    for i in range(len(mean_value)):
        sum_value.append(mean_value[i]*weight_value[i])
    return sum(sum_value)/sum(weight_value)
weighted_mean_function = weighted_mean(houses_per_year['Mean Price'],houses_per_year['Houses Sold'])
from numpy import average
weighted_mean_numpy = average(houses_per_year['Mean Price'],weights=houses_per_year['Houses Sold'])
equal = round(weighted_mean_function,10) == round(weighted_mean_numpy,10)
                              
## 4. The Median for Open-ended Distributions ##

distribution1 = [23, 24, 22, '20 years or lower,', 23, 42, 35]
distribution2 = [55, 38, 123, 40, 71]
distribution3 = [45, 22, 7, '5 books or lower', 32, 65, '100 books or more']
median1 = 23
median2 = 55
median3 = 32

## 5. Distributions with Even Number of Values ##

TotRms = houses['TotRms AbvGrd'].copy()
TotRms = TotRms.replace('10 or more','10')
TotRms = TotRms.astype(int)
TotRms = TotRms.sort_values()
middle_indices = [int(len(TotRms)/2)-1,int(len(TotRms)/2)]
middle_values = TotRms.iloc[middle_indices]
median = middle_values.mean()

## 6. The Median as a Resistant Statistic ##

houses['Lot Area'].plot.box()
houses['SalePrice'].plot.box()
Lot_mean = houses['Lot Area'].mean()
Lot_median = houses['Lot Area'].median()
SalePrice_mean = houses['SalePrice'].mean()
SalePrice_median = houses['SalePrice'].median()
lotarea_difference = Lot_mean-Lot_median
saleprice_difference = SalePrice_mean-SalePrice_median

## 7. The Median for Ordinal Scales ##

mean = houses['Overall Cond'].mean()
median = houses['Overall Cond'].median()
houses['Overall Cond'].plot.hist()
more_representative = 'mean'