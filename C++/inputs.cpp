#include <iostream>
#include <math.h>
#include <algorithm>

// #include <array>
using namespace std;


double add_two_array_values(int a[], int i, int j, int n)
{
    if (i < 0 || i >= n || j < 0 || j >= n)
    {
        return -100000;
    }
    else {
        return (a[i] + a[j]) / 2;
    }
    
}

int add_values( int a[], int n){
    int sum = 0;

    for (int i = 0; i < n; i++)
    {
        sum += a[i];
    }
    return sum;    
}

int* array_calc1(int a[], int k, int n){
    int i;
    static int b[10000];
    for (int i = 0; i < n; i++)
    {
        b[i] = a[i]/k;
    }
    return b; 
}

int* array_copy(int a[], int n){
    int i;
    static int b[1000];
    for(int i = 0; i < n; i++){
        b[i] = a[i];
    }

    return b;
}

double autoCorrelation(double data[], int lag, double mean, double variance, int n){
    double run = 0;
    for (int i = lag; i < n; i++)
    {
        run += (data[i] - mean) * (data[i - lag] - mean);
    }
    
    return run / (n - lag) / variance;
}

double average(float a[], int n){
    double suma = 0;
    for (int i = 0; i < n; i++)
    {
        suma += a[i];
    }
    
    return suma/n;
}

int binarySearchFromTo(double elements[], double key, int from, int to){
    int low = from;
    int high = to;
    while (low <= high)
    {
        int mid = (low + high) / 2;
        double midVal = elements[mid];

        if (midVal < key)
        {
            low = mid + 1;
        } else{
            if (midVal > key)
            {
                high = mid -1;
            } else
            {
                return mid;
            }          
        }
    }
    return - (low +1);
}

int* bubble(int a[], int n){
    int i, j, t;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            if (a[j] > a[j + 1])
            {
                t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
            }
        }
    }
    return a;
}

double* calculateAbsoluteDifferences(double z[], int n){

    if (n == 0)
    {
        return NULL;
    }
    
    static double zAbs[100];
    for (int i = 0; i < n; i++)
    {
        zAbs[i] = abs(z[i]);
    }
    return zAbs;
}

double* calculateDifferences(double x[], double y[], int n){

    static double z[100];

    for (int i = 0; i < n; i++)
    {
        z[i] = y[i] - x[i];
    }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    
    return z;
}

double chebyshevDistance(double p1[], double p2[], int n1, int n2){
    if (n1 !=  n2)
    {
        cout << "Error!" << endl;
        return 0;
    }

    double maxDiff = abs(p1[0] - p2[0]);
    for (int i = 1; i < n1; i++)
    {
        double diff = p1[i] - p2[i];
        if (maxDiff < diff)
        {
            maxDiff = diff;
        }
    }
    return maxDiff;        
}

bool check_equal_tolerance(double a[], double b[], double tol, int n1, int n2){
    if (n1 != n2)
    {
        return false;
    }
    for (int i = 0; i < n1; i++)
    {
        if (abs(a[i] - b[i]) >= tol)
        {
            return false;
        }
    }
    return true; 
}

bool check_equal(double a[], double b[], int n1, int n2){
    if (n1 != n2)
    {
        return false;
    }
    for (int i = 0; i < n1; i++)
    {
        if (a[i] != b[i])
        {
            return false;
        }
    }
    return true; 
}

bool checkPositive(double a[], int n){
    
    for (int i = 0; i < n; i++)
    {
        if (a[i] <= 0)
        {
            return false;
        }
    }
    return true; 
}

bool checkNonNegative(double a[], int n){
    
    for (int i = 0; i < n; i++)
    {
        if (a[i] < 0)
        {
            return false;
        }
    }
    return true; 
}

double chiSquate(double expected[], double observed[], int n){
    double sumExpected = 0;
    double sumObserved = 0;
    for (int i = 0; i < n; i++) {
        sumExpected += expected[i];
        sumObserved += observed[i];
        }
    double ratio = 1.0;
    bool rescale = false;
    if (abs(sumExpected - sumObserved) > 10E-6) {
        ratio = sumObserved / sumExpected;
        rescale = true;
    }
    double sumSq = 0.0;
    for (int i = 0; i < n; i++) {
        if (rescale) {
            double dev = observed[i] - ratio * expected[i];
            sumSq += dev * dev / (ratio * expected[i]);
        } else {
            double dev = observed[i] - expected[i];
            sumSq += dev * dev / expected[i];
            }
        }
    return sumSq;
}

int* clip(int a[], int lowerLim, int upperLim, int n) {
    static int r[100];
        for (int i = 0; i < n; i++) {
            if (a[i] < lowerLim) {
                r[i] = lowerLim;
            } else {
                if (a[i] > upperLim) {
                    r[i] = upperLim;
                } else {
                    r[i] = a[i];
                }
            }
        }
    return r;
}

int cnt_zeroes(int a[], int n){
    int cnt = 0;
    for (int i = 0; i < n; i++)
    {
        if (a[i] == 0)
        {
            cnt ++;
        }
    }
    return cnt;
}

double computeCanberraDistance(double a[], double b[], int n) {
    double sum = 0;
    for (int i = 0; i < n; i++) {
        double num = abs(a[i] - b[i]);
        double denom = abs(a[i]) + abs(b[i]);
        sum += num == 0.0 && denom == 0.0 ? 0.0 : num / denom;
    }
    return sum;
}

double* computeDividedDifference1(double x[], double y[], int n) {
    double divdiff[1000];
    static double a[100];
    a[0] = y[0];
    
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < n - i; j++) {
            double denominator = x[j + i] - x[j];
            y[j] = (y[j + 1] - y[j]) / denominator;
        }
        a[i] = y[0];
    }
    return a;
}

double cosineDistance(double p1[], double p2[], int n) {
    double dotProduct = 0.0;
    double lengthSquaredp1 = 0.0;
    double lengthSquaredp2 = 0.0;

    for (int i = 0; i < n; i++) {
        lengthSquaredp1 += p1[i] * p1[i];
        lengthSquaredp2 += p2[i] * p2[i];
        dotProduct += p1[i] * p2[i];
    }
    
    double denominator = sqrt(lengthSquaredp1) * sqrt(lengthSquaredp2);
    if (denominator < dotProduct) {
        denominator = dotProduct;
    }
    if (denominator == 0 && dotProduct == 0) {
        return 0;
    }
    return 1.0 - dotProduct / denominator;
}

int count_k(int a[], int k, int n) {
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] == k) {
            cnt++;
        }
    }
    return cnt;
}

int count_non_zeroes(int a[], int n) {
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] != 0) {
            cnt++;
        }
    }
    return cnt;
}

double covariance(double elements1[], double elements2[], int n) {

    double sumx = elements1[0];
    double sumy = elements2[0];
    double Sxy = 0;
    
    for (int i = 1; i < n; ++i) {
        double x = elements1[i];
        double y = elements2[i];
        sumx += x;
        Sxy += (x - sumx / (i + 1)) * (y - sumy / i);
        sumy += y;
    }
    return Sxy / (n - 1);
}

int* dec_array(int a[], int k, int n) {
    for (int i = 0; i < n; i++) {
        a[i] -= k;
    }
    return a;
}

double distance1(double p1[], double p2[], int n) {
    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += abs(p1[i] - p2[i]);
    }
    return sum;
}

double distanceInf(double p1[], double p2[], int n) {
    double maxi = 0;
    for (int i = 0; i < n; i++) {
        maxi = max(maxi, abs(p1[i] - p2[i]));
    } 
    return maxi;
}

int dot_product(int a[], int b[], int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
            sum += a[i] * b[i];
        }
    return sum;
}

double durbinWatson(double elements[], int n) {
    
    double run = 0;
    for (int i = 1; i < n; ++i) {
        double x = elements[i] - elements[i - 1];
        run += x * x;
    }
    return run;
}

double* ebeAdd(double a[], double b[], int n1, int n2) {
    if (n1 != n2) {
        return NULL;
    }
    static double  result[1000];
    for (int i = 0; i < n1; i++) {
        result[i] = a[i] + b[i];
        }
    return result;
}

double* ebeDivide(double a[], double b[], int n1, int n2) {
    if (n1 != n2) {
        return 0;
    }
    static double  result[1000];
    for (int i = 0; i < n1; i++) {
        result[i] =  a[i]/b[i];
    }
    return result;
}

double*  ebeMultiply(double a[], double b[], int n1, int n2) {
    if (n1 != n2) {
        return 0;
    }
    static double  result[1000];
    for (int i = 0; i < n1; i++) {
        result[i] =  a[i]*b[i];
    }
    return result;
}

double*  ebeSubtract(double a[], double b[], int n1, int n2) {
    if (n1 != n2) {
        return 0;
    }
    static double  result[1000];
    for (int i = 0; i < n1; i++) {
        result[i] =  a[i] - b[i];
    }
    return result;
}

bool* elementwise_equal(int a[], int b[], int n) {
    static bool r[1000];
    for (int i = 0; i < n; i++) {
        if (a[i] == b[i]) {
            r[i] = true;
        } else {
            r[i] = false;
        }
    }
    return r;
}

int* elementwise_max(int a[], int b[], int n) {
    static int r[1000];
    for (int i = 0; i < n; i++) {
        if (a[i] > b[i]) {
            r[i] = a[i];
        } else {
            r[i] = b[i];
        }
    }
    return r;
}

int* elementwise_min(int a[], int b[], int n) {
    static int r[1000];
    for (int i = 0; i < n; i++) {
        if (a[i] < b[i]) {
            r[i] = a[i];
        } else {
            r[i] = b[i];
        }
    }
    return r;
}

bool* elementwise_not_equal(int a[], int b[], int n){
    static bool r[1000];
    for (int i = 0; i < n; i++) {
        if (a[i] != b[i]) {
            r[i] = true;
        } else {
            r[i] = false;
        }
    }
    return r;
}

double entropy(double k[], int n){
    double h = 0;
    double sum_k = 0;
    for (int i = 0; i < n; i++) {
        sum_k += (double) k[i];
    }
    for (int i = 0; i < n; i++) {
        if (k[i] != 0) {
            double p_i = (double) k[i] / sum_k;
            h += p_i * log(p_i);
        }
    }
    return -h;
}

bool equals(double x[], double y[], int nx, int ny) {

    if (nx != ny) {
        return false;
    }
    for (int i = 0; i < nx; ++i) {
        if (abs(y[i] - x[i]) > 0.0001) {
            return false;
        }
    }
    return true;
}

double errorRate(double labels[], double predictions[], int n) {
    double nberrors = 0;
    double datasize = 0;
    for (int index = 0; index < n; index++) {
        if (predictions[index] == -1) {
            continue;
        }
        if (predictions[index] != labels[index]) {
            nberrors++;
        }
        datasize++;
    }
    return nberrors / datasize;
}

double evaluateHoners(double coefficients[], double argument, int n) {
    
    double result = coefficients[n - 1];
    for (int j = n - 2; j >= 0; j--) {
        result = argument * result + coefficients[j];
    }
    return result;
}

double evaluateInternal(double x[], double y[], double z, int n) {
    int nearest = 0;
    double c[1000];
    double d[1000];
    double min_dist = INFINITY;
    for (int i = 0; i < n; i++) {
        c[i] = y[i];
        d[i] = y[i];
        double dist = abs(z - x[i]);
        if (dist < min_dist) {
            nearest = i;
            min_dist = dist;
        }
    }
    double value = y[nearest];
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < n - i; j++) {
            double tc = x[j] - z;
            double td = x[i + j] - z;
            double divider = x[j] - x[i + j];
            double w = (c[j + 1] - d[j]) / divider;
            c[j] = tc * w;
            d[j] = td * w;
        }
        if (nearest < 0.5 * (n - i + 1)) {
            value += c[nearest];
        } else {
            nearest--;
            value += d[nearest];
        }
    }
    return value;
}

double evaluateNewton(double a[], double c[], double z, int nc) {
    int n = nc - 1;
    double value = a[n];
    for (int i = n - 1; i >= 0; i--) {
        value = a[i] + (z - c[i]) * value;
    }
    return value;
}

double evaluateWeightedProduct( double values[],  double weights[],  int begin, int lengths, int n) {
    double product = 1.0;
     
    for (int i = begin; i < begin + lengths; i++) {
        product *= pow(values[i], weights[i]);
    }
    return product;
}

int*  find_diff(int a[], int b[], int na) {
    static int c[1000];
    for (int i = 0; i < na; i++) {
        c[i] = a[i] - b[i];
    }
    return c;
}

double find_euc_dist(int a[], int b[], int na) {
    double sum = 0;
    for (int i = 0; i < na; i++) {
        sum += (a[i] - b[i]) * (a[i] - b[i]);
    }
    double result = sqrt(sum);
    return result;
}

double find_magnitude(int a[], int n) {
    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += a[i] * a[i];
    }
    double result = sqrt(sum);
    return result;
}

int find_max(int a[], int n) {
    int max = a[0];
    for (int i = 0; i < n; i++) {
        if (a[i] > max) {
            max = a[i];
        }
    }
    return max;
}

int find_max2(int a[], int n) {
    int max = a[0] + a[1];
    for (int i = 0; i < n - 1; i++) {
        if (a[i] + a[i + 1] > max) {
            max = a[i] + a[i + 1];
        }
    }
    return max;
}

double find_median(int a[], int n) {
    int k = n / 2 + 1;
    int minIndex = 0;
    int minValue = a[0];
    for (int i = 0; i < k; i++) {
        minIndex = i;
        minValue = a[i];
        for (int j = i + 1; j < n; j++) {
            if (a[j] < minValue) {
                minIndex = j;
                minValue = a[j];
            }
        }
        int temp = a[i];
        a[i] = a[minIndex];
        a[minIndex] = temp;
    }
    if (n % 2 == 0) {
        return (double) (a[n / 2 - 1] + a[n / 2]) / 2;
    } else {
        return a[n / 2];
    }
}

int find_min(int a[], int n) {
    int min = a[0];
    int i;
    for (i = 0; i < n; i++) {
        if (a[i] < min) {
            min = a[i];
        }
    }
    return min;
}

double g( double expected[],  double observed[], int n) {
    double sumExpected = 0;
    double sumObserved = 0;
    for (int i = 0; i < n; i++) {
        sumExpected += expected[i];
        sumObserved += observed[i];
    }
    double ratio = 1;
    bool rescale = false;
    if (abs(sumExpected - sumObserved) > 10E-6) {
        ratio = sumObserved / sumExpected;
        rescale = true;
    }
    double sum = 0;
        for (int i = 0; i < n; i++) {
            double dev = rescale ? log((double) observed[i] / (ratio * expected[i])) : log((double) observed[i] / expected[i]);
            sum += (double) observed[i] * dev;
        }
    return 2 * sum;
}

double geometric_mean(int a[], int n) {
    long product = 1;
    for (int i = 0; i < n; i++) {
        product *= a[i];
    }
    return pow(product, (double) 1 / n);
}

int get_array_value(int a[], int k, int n) {
    if(k - 1 >= n || k - 1 < 0) {
        return -100000;
    } else {
        return a[k - 1];
    }
}

int hamming_dist(int a[], int b[], int n) {
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] != b[i]) {
            cnt++;
        }
    }
    return cnt;
}

double harmonicMean(double data[], int n) {
    double sumOfInversions = 0;
    for (int i = 0; i < n; i++) {
        sumOfInversions += 1 / data[i];
    }
    return n / sumOfInversions;
}

int* insertion_sort(int array[], int n) {
    for (int i = 1; i < n; i++) {
        int j = i;
        int B = array[i];
        while (j > 0 && array[j - 1] > B) {
            array[j] = array[j - 1];
            j--;
        }
        array[j] = B;
        }
    
    return array;
}

double kurtosis(double data[], int n) {
    double sum = 0;
    double sumPD = 0;
    double sumSq = 0;
    for (int i = 0; i < n; i++) {
        sum += data[i];
        sumSq += data[i] * data[i];
    }
    double mean = sum / n;
    double standardDeviation = sqrt((sumSq - mean * sum) / n);
    for (int i = 0; i < n; i++) {
        sumPD += pow(data[i] - mean, 4);
    }
    double moment4 = sumPD / n;
    return -3 + moment4 / (standardDeviation * standardDeviation * standardDeviation * standardDeviation);
}

double lag1(double elements[], double mean, int n){
    double r1;
    double q = 0;
    double v = (elements[0] - mean) * (elements[0] - mean);
    for (int i = 1; i < n; i++) {
        double delta0 = elements[i - 1] - mean;
        double delta1 = elements[i] - mean;
        q += (delta0 * delta1 - q) / (i + 1);
        v += (delta1 * delta1 - v) / (i + 1);
    }
    r1 = q / v;
    return r1;
}

double manhattan_dist(int a[], int b[], int n) {
    int i;
    double sum = 0;
    for (i = 0; i < n; i++) {
        sum += abs(a[i] - b[i]);
    }
    return sum;
}

double manhattanDistance(double p1[], double p2[], int n) {
    double result = 0.0;
    for (int i = 0; i < n; i++) {
        result += abs(p2[i] - p1[i]);
    }
    return result;
}

double max(double elements[], int n) {
    int size = n;
    double max = elements[size - 1];
    for (int i = size - 1; --i >= 0; ) {
        if (elements[i] > max) {
            max = elements[i];
        }
    }
    return max;
}

double mean_absolute_error(int a[], int b[], int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += abs(a[i] - b[i]);
    }
    return (double) sum / n;
}

double meanDeviation(double elements[], double mean, int n) {
    int size = n;
    double sum = 0;
    for (int i = size; --i >= 0; ) {
        sum += abs(elements[i] - mean);
    }

    return sum / size;
}

double meanDifference(double sample1[], double sample2[], int n ) {
    double sumDifference = 0;
    for (int i = 0; i < n; i++) {
        sumDifference += sample1[i] - sample2[i];
    }

    return sumDifference / n;
}

double min(double elements[], int n) {
    int size = n;
    double min = elements[size - 1];
    for (int i = size - 1; --i >= 0; ) {
        if (elements[i] < min) {
            min = elements[i];
        }
    }

    return min;
}

int partition(double work[], int begin, int end, int pivot) {
    double value = work[pivot];
    work[pivot] = work[begin];
    int i = begin + 1;
    int j = end - 1;
    while (i < j) {
        while (i < j && work[j] > value) {
            --j;
        }
        while (i < j && work[i] < value) {
            ++i;
        }
        if (i < j) {
            double tmp = work[i];
            work[i++] = work[j];
            work[j--] = tmp;
        }
    }
    if (i >= end || work[i] > value) {
        --i;
    }
    work[begin] = work[i];
    work[i] = value;

    return i;
}

double polevl(double x, double coef[], int N){    
    double ans1;
    ans1 = coef[0];
    
    for (int i = 1; i <= N; i++) {
        ans1 = ans1 * x + coef[i];
    }

    return ans1;
}

double pooledMean(double data1[], double data2[], int n1, int n2) {
    double sum1 = 0;
    for (int i = 0; i < n1; i++) {
        sum1 += data1[i];
    }
    double mean1 = sum1 / n1;
    double sum2 = 0;
    for (int i = 0; i < n2; i++) {
        sum2 += data2[i];
    }
    double mean2 = sum2 / n2;

    return (n1 * mean1 + n2 * mean2) / (n1 + n2);
}

double pooledVariance(double data1[], double data2[], int n1, int n2) {
    double sum1 = 0;
    double sumSq1 = 0;
    for (int i = 0; i < n1; i++) {
        sum1 += data1[i];
        sumSq1 += data1[i] * data1[i];
    }
    double mean1 = sum1 / n1;
    double var1 = (sumSq1 - mean1 * sum1) / n1;
    double sum2 = 0;
    double sumSq2 = 0;
    for (int i = 0; i < n2; i++) {
        sum2 += data2[i];
        sumSq2 += data2[i] * data2[i];
    }
    double mean2 = sum2 / n2;
    double var2 = (sumSq2 - mean2 * sum2) / n2;

    return (n1 * var1 + n2 * var2) / (n1 + n2);
}

double* power(double data[], int k, int n) {
    for (int i = 0; i < n; i++) {
        data[i] = pow(data[i], k);
    }
    return data;
}

double product(double elements[], int n) {
    int size = n;
    double product = 1;
    for (int i = size; --i >= 0; ) {
        product *= elements[i];
    }
    return product;
}

double quantile(double sortedElements[], double phi, int n) {      
    double index = phi * (n - 1);
    int lhs = (int) index;
    double delta = index - lhs;
    double result;
    if (n == 0) {
        return 0.0;
    }
    if (lhs == n - 1) {
        result = sortedElements[lhs];
    } else {
        result = (1 - delta) * sortedElements[lhs] + delta * sortedElements[lhs + 1];
    }
    return result;
}

int* reverse(int a[], int n) {
    static int r[1000];
    int cnt = 0;
    for (int i = n - 1; i >= 0; i--) {
        r[cnt] = a[i];
        cnt++;
    }
    return r;
}

double safeNorm(double v[], int n) {
    double rdwarf = 3.834e-20;
    double rgiant = 1.304e+19;
    double s1 = 0;
    double s2 = 0;
    double s3 = 0;
    double x1max = 0;
    double x3max = 0;
    double floatn = n;
    double agiant = rgiant / floatn;
    
    for (int i = 0; i < n; i++) {
        double xabs = abs(v[i]);
        if (xabs < rdwarf || xabs > agiant) {
            if (xabs > rdwarf) {
                if (xabs > x1max) {
                    double r = x1max / xabs;
                    s1 = 1 + s1 * r * r;
                    x1max = xabs;
                } else {
                    double r = xabs / x1max;
                    s1 += r * r;
                }
            } else {
                if (xabs > x3max) {
                    double r = x3max / xabs;
                    s3 = 1 + s3 * r * r;
                    x3max = xabs;
                } else {
                    if (xabs != 0) {
                        double r = xabs / x3max;
                        s3 += r * r;
                    }
                }
            }
        } else {
            s2 += xabs * xabs;
        }
    }
    double norm;
    if (s1 != 0) {
        norm = x1max * sqrt(s1 + s2 / x1max / x1max);
    } else {
        if (s2 == 0) {
            norm = x3max * sqrt(s3);
        } else {
            if (s2 >= x3max) {
                norm = sqrt(s2 * (1 + x3max / s2 * (x3max * s3)));
            } else {
                norm = sqrt(x3max * (s2 / x3max + x3max * s3));
            }
        }
    }
    return norm;
}

double sampleKurtosis(int size, double moment4, double sampleVariance) {
    int n = size;
    double s2 = sampleVariance;
    double m4 = moment4 * n;

    return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3));
}

double sampleSkew(int size, double moment3, double sampleVariance) {
    int n = size;
    double s = sqrt(sampleVariance);
    double m3 = moment3 * n;

    return n * m3 / ((n - 1) * (n - 2) * s * s * s);
}

double sampleVariance(double elements[], double mean, int n) {
    int size = n;
    double sum = 0;
    for (int i = size; --i >= 0; ) {
        double delta = elements[i] - mean;
        sum += delta * delta;
    }
    return sum / (size - 1);
}

double sampleWeightedVariance(double data[], double weights[], int n) {
    double sumOfWeights = 0;
    double sumOfProducts = 0;
    double sumOfSquaredProducts = 0;
    for (int i = 0; i < n; i++) {
        sumOfWeights += weights[i];
        sumOfProducts += data[i] * weights[i];
        sumOfSquaredProducts += data[i] * data[i] * weights[i];
    }
    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 1);
}

double* scale(double val, double arr[], int n) {
    static double  newArr[1000];

    for (int i = 0; i < n; i++) {
        newArr[i] = arr[i] * val;
    }
    return newArr;
}

int* selection_sort(int list[], int n) {
    int i;
    int j;
    int min;
    for (i = 0; i < n - 1; i++) {
        min = i;
        for (j = i + 1; j < n; j++) {
            if (list[j] < list[min]) {
                min = j;
            }
        }
        int tmp = list[i];
        list[i] = list[min];
        list[min] = tmp;
    }
    return list;
}

int sequential_search(int a[], int key, int n) {
    int i;
    for (i = 0; i < n; i++) {
        if (a[i] == key) {
            return i;
        }
    }
    return -1;
}

int* set_min_val(int a[], int k, int n) {
    int i;
    for (i = 0; i < n; i++) {
        if (a[i] < k) {
            a[i] = k;
        }
    }
    return a;
}

int* shell_sort(int a[], int n) {
    int j;
    int i;
    int k;
    int m;
    int mid;
        
    for (m = n/2; m > 0; m /= 2) {
        for (j = m; j < n; j++) {
            for (i = j - m; i >= 0; i -= m) {
                if (a[i + m] >= a[i]) {
                    break;
                } else {
                    mid = a[i];
                    a[i] = a[i + m];
                    a[i + m] = mid;
                }
            }
        }
    }
    return a;
}

double skew(double data[], int n) {
    double sum = 0;
    double sumPD = 0;
    double sumSq = 0;
    for (int i = 0; i < n; i++) {
        sum += data[i];
        sumSq += data[i] * data[i];
    }
    double mean = sum / n;
    double standardDeviation = sqrt((sumSq - mean * sum) / n);
    for (int i = 0; i < n; i++) {
        sumPD += pow(data[i] - mean, 3);
    }
    double moment3 = sumPD / n;
    
    return moment3 / (standardDeviation * standardDeviation * standardDeviation);
}

double* square(double data[], int n) {
    for (int i = 0; i < n; i++) {
        data[i] = data[i] * data[i];
    }
    return data;
}

double* standardize(double data[], int n) {
    double sum = 0;
    double sumSq = 0;
    for (int i = 0; i < n; i++) {
        sum += data[i];
        sumSq += data[i] * data[i];
    }
    double mean = sum / n;
    double sd = sqrt((sumSq - mean * sum) / n);
    for (int i = 0; i < n; i++) {
        data[i] = (data[i] - mean) / sd;
    }
    return data;
}

int sum(int values[], int n) {
    int sum = 0;
    for(int i= 0 ; i < n ; i++) {
        sum += values[i];
    }
    return sum;
}

double sumOfLogarithms(double elements[], int n) {
    double logsum = 0;
    for(int i = 0; i < n; i++) {
        logsum += log(elements[i]);
    }
    return logsum;
}

double sumOfPowerOfDeviations(double data[], int k, double c, int n) {
    double sum = 0;
    for(int i = 0; i < n; i++) {
        sum += pow(data[i] - c, k);
        }
    return sum;
}

double tanimotoDistance(double p1[], double p2[], int n) {
    double ab = 0;
    double aSq = 0;
    double bSq = 0;
    for (int i = 0; i < n; i++) {
        ab += p1[i] * p2[i];
        aSq += p1[i] * p1[i];
        bSq += p2[i] * p2[i];
    }
    double denominator = aSq + bSq - ab;
    if (denominator < ab) {
        denominator = ab;
    }
    if (denominator > 0) {
        return 1.0 - ab / denominator;
    } else {
        return 0.0;
    }
}

double variance(double x[], int n) {
    double sum = 0;
    double sum1 = 0;
    double var = 0;
    double avrg = 0;
    for(int i = 0; i < n; i++) {
        sum = sum + x[i];
    }
    
    avrg = sum / (double)n;
    for (int i = 0; i < n; i++) {
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg);
    }
    var = sum1 / (double) n;
    return var;
}

double varianceDifference(double sample1[], double sample2[], int n) {
    double sum1 = 0;
    double sum2 = 0;
    double diff = 0;
    double sumDifference = 0;

    for (int i = 0; i < n; i++) {
        sumDifference += sample1[i] - sample2[i];
    }
    
    double meanDifference = sumDifference / n;
    for (int i = 0; i < n; i++) {
        diff = sample1[i] - sample2[i];
        sum1 += (diff - meanDifference) * (diff - meanDifference);
        sum2 += diff - meanDifference;
    }
    return (sum1 - sum2 * sum2 / n) / (n - 1);
}

double weighted_average(double a[], double b[], int n) {
    double sum1 = 0;
    double sum2 = 0;
    for(int i = 0; i < n; i++) {
        sum1 += a[i] * b[i];
        sum2 += b[i];
    }
    return sum1 / sum2;
}

double weightedMean(double elements[], double theWeights[], int n) {
    int size = n;
    double sum = 0.0;
    double weightsSum = 0.0;
    for(int i = size; --i >= 0; ) {
        double w = theWeights[i];
        sum += elements[i] * w;
        weightsSum += w;
    }
    return sum / weightsSum;
}

double weightedRMS(double data[], double weights[], int n) {
    double sumOfProducts = 0;
    double sumOfSquaredProducts = 0;
    for(int i = 0; i < n; i++) {
        sumOfProducts += data[i] * weights[i];
        sumOfSquaredProducts = data[i] * data[i] * weights[i];
    }
    return sumOfProducts / sumOfSquaredProducts;
}

double winsorizedMean(double sortedElements[], int left, int right, int n) {

    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += sortedElements[i];
    }
    double mean = sum / n;
    double leftElement = sortedElements[left];
    for (int i = 0; i < left; ++i) {
        mean += (leftElement - sortedElements[i]) / n;
    }
    double rightElement = sortedElements[n - 1 - right];
    for (int i = 0; i < right; ++i) {
        mean += (rightElement - sortedElements[N - 1 - i]) / n;
    }
    return mean;
}

int main()
{
    int arr[] = {12, 3, 4, 15, 100};
    int al = sizeof(arr)/sizeof(arr[0]);
    // cout << al << '\n';
    
    double array[] = {12, -3, 4, -15, 100};
    int n = sizeof(array)/sizeof(array[0]);
    // cout << "RESULT " << add_two_array_values(arr, 0, 2, al);
    // cout << "RESULT:  " << add_values(arr, al);
    int *arry_result;
    double *arr_results;
    bool *arr_result_bool;
    // arry_result = array_calc1(arr, 2 , al);
    // arry_result = array_copy(arr, al);
    // cout << *arry_result;
    
    arr_results = calculateAbsoluteDifferences(array, n);


    int p1[] = {1, 6, 3};
    int p2[] = {1, -11, 3};
    int np1 = sizeof(p1)/sizeof(p1[0]);
    int np2 = sizeof(p2)/sizeof(p2[0]);
    // cout << chebyshevDistance(p1, p2, 3, 4) << endl;
    // cout << check_equal_tolerance(p1,p2, 2, 3, 3) << endl;
    // cout << check_equal(p1,p2, np1, np2) << endl;
    // cout << distanceInf(p1, p2, 3) << endl;
    // cout << chiSquate(p1, p2, 3) << endl;
    arr_result_bool = elementwise_equal(p1,p2,3);
    
    for (int i = 0; i < 3; i++)
    {
        /* code */
        cout << "RESULT:  " << *(arr_result_bool + i) << endl;
    }
    
    return 0;
}

