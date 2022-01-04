import numpy as np

def find_local_maximum(image_hist, n):
    size = len(image_hist)
    nhalf = n // 2
    # Rcpp::LogicalVector tmp(size);
    tmp = np.zeros(size)
    count = 0
    # std::list< std::pair<int,double> > window;
    window = []
    # std::pair<int,double> max_elem = std::make_pair(0,0.0);
    max_elem = [0,np.double(0.0)]
    
    for i in range(0,nhalf+1):#int i = 0; i <= nhalf; ++i:
        if (i < size):
            # std::pair<int,double> tmp_pair = std::make_pair(i,hist[i]);
            tmp_pair = [i,image_hist[i]]
            window.append(tmp_pair);
            if (image_hist[i] > max_elem[1]):
                max_elem[0] = i;
                max_elem[1] = image_hist[i];
    if (max_elem[0] == nhalf):
        tmp[nhalf] = True;
        count+=1
    sizeminhalf = size - nhalf;

    for i in range(nhalf+1, sizeminhalf): #(int i = nhalf + 1; i < sizeminhalf; ++i)
        max_range = i + nhalf;
        window.pop(0); 
        
        # std::pair<int,double> tmp_pair = std::make_pair(max_range,hist[max_range]);
        tmp_pair = [max_range, image_hist[max_range]]
        
        window.append(tmp_pair);
        
        if (image_hist[max_range] > max_elem[1]):
            max_elem[0] = max_range;
            max_elem[1] = image_hist[max_range];

        if (max_elem[0] < i - nhalf):
            # std::pair<int,double> tmp_first = *(window.begin());
            max_elem[0] = window[0][0]
            max_elem[1] = window[0][1]
            
            # for (std::list< std::pair<int,double> >::iterator itr = window.begin(); itr != window.end(); ++itr):
            for first,second in window:
                # std::pair<int,double> tmp_pair = *itr;
                if (second > max_elem[1]):
                    max_elem[0] = first
                    max_elem[1] = second
        if (max_elem[0] == i):
            tmp[i] = True;
            count += 1
    # Rcpp::NumericVector res(count);
    res = np.zeros(count)
    if (count > 0):
        tmp_count = 0
        for i in range(0,size): #(int i = 0; i < size; ++i)
            if (tmp[i]):
                res[tmp_count] = image_hist[i];
                tmp_count += 1
    return res;