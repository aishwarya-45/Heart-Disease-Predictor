## Heart-Disease-Predictor
INTRODUCTION:

There is enormous progress in keeping the record of human health electronically by healthcare facilities and in this, perfection is a priority. Now, as the data is huge it is not possible for healthcare providers to use the information efficiently and this is where artificial intelligence is realized to be exceptionally effective.
Heart diseases are one of the most common diseases out there which are accountable for >80% of deaths. So, if these diseases can be predicted well in advance, they can provide important insights to doctors who can then adapt their diagnosis and treatment per patient basis.
Besides, this low cost model will cut down on a lot of expenses that would have otherwise been spent on various heart disease testing. Whereas, with this, the user just needs to fill in the form to get the result without having to spend on any tests.
Note: The scope of our model is upto predicting, if the user has got any heart disease or not, but doesn‟t particularly tell about which heart disease.

ALGORITHMS APPLIED: 

In this project we‟ve used supervised machine learning algorithms to predict the possibility of a heart disease. We have used the hear.csv dataset from UCI Machine Learning Repository . This dataset has a total of 14 attributes Hence this research work also intended to use only the 14 attributes. 
The various attributes and their description are as follows:
age: Age of patient (in years)
sex: Gender of patient (divided into two categories: 1 for male and 0 for female)
trestbps: Resting blood pressure (in mm Hg))
cp: Type of chest pain (divided into four categories: 1 for typical angina, 2 for atypical angina, 3 for non- anginal pain, and 4 for asymptomatic)
chol: Cholesterol level (in mg/dl)
fbs: Blood sugar level at fasting mode (empty stomach) (divided into two categories: 1 for true and 0 for false)
thalach: The maximum heart rate attained by patient
restECG: Electrocardiographic (ECG) results at rest
exang: Exercise induced angina (divided into two categories: 1 for yes and 0 for no)
old peak: ST depression induced angina
slope: Peak exercise ST segment slope (divided into three categories: 1 for upsloping, 2 for flat and 3 for downsloping)
ca thal: Number (0-3) of major vessels colored by fluoroscopy
target: Heart status (divided into three categories: 3 for normal, 6 for fixed defect, 7 for reversible defect)

Under supervised learning methods, since we were classifying a user into a patient and non-patient, we experimented with classification models.
So, in this project we‟ve used classification models like, decision tree and KNN to predict heart diseases and compare their performance.

EXPERIMENTS: 

1. We divided the dataset into two parts
● Training dataset: this dataset performs training of models by ML algorithm, we took the dataset
and made 80% of it as a training dataset.
● Testing dataset: this data set tests the performance of the trained model.

2. Then we did feature scaling using the Standard scaler library.
Standard scaler: StandardScaler assumes your data is normally distributed within each feature and will scale them such that the distribution is now centred around 0, with a standard deviation of 1. The mean and standard deviation are calculated for the feature and then the feature is scaled based on: Xi – mean(X)/SD(X).

3. Then we evaluated the model on two different ML algorithms that are, decision tree algorithm and KNN algorithm.

OBSERVATIONS:

We got 78.6% accuracy in “decision tree algorithm” which is not a reliable accuracy for healthcare since it‟s a sensitive issue. So we used the “KNN algorithm” and got 90.16% accuracy. This has a better accuracy so we chose this algorithm to design our model.
Secondly, this model cuts down on time and expenses that otherwise would have been spent on clinical testing for heart disease. So, in a way, this model is an efficient solution in predicting heart diseases.

![AI_predictor](https://user-images.githubusercontent.com/68557476/112708188-9fcba100-8ed6-11eb-8a89-d04569bf8be1.png)


CONCLUSIONS:

Heart disease is the most common disease in India. Determining any heart disease on some raw data is really difficult for even a doctor which is why many healthcare sectors are opting for machine learning techniques to determine it.
Early detection of heart diseases will increase the survival rate and that‟s what our project intends to achieve. Our project predict whether the patient has heart disease or not with the help of clinical data which will assist the diagnosis process. Three supervised machine learning algorithms namely KNN algorithm and Decision tree algorithm are compared in terms of accuracy using the heart diseases dataset. From the experimental results it‟s evident that KNN algorithm predicts heart disease with the accuracy of 90.16%.
