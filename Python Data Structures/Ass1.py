'''
 Write code using find() and string slicing to extract the number at the end of the line below.
 Convert the extracted value to a floating point number and print it out.
 '''
 text = "X-DSPAM-Confidence:    0.8475";
indx = text.find('0');
output = text[indx:(indx+6)];
print(float(output));
