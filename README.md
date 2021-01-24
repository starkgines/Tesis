# Tesis 

TKC
How to work in this project
Create a enviroment with anaconda prompt *conda create -n tesis
Then you need to install jupyter notebook
with pip : pip install jupyterlab
with conda : conda install -c conda-forge jupyterlab
add the enviroment to the kernel
activate tesis
ipython kernel install --name "tesis" --user
install all dependence
MobaXterm
User and Pass
User : ssh -X -p 22000 dlconnie@200.10.231.198
Pass : dlconnie@2020
source venv/bin/activate
How to run and read with root in MobaXterm
$nohup ./muonModel primary.mac > log 2> loger
if you want to see the progress: $ps -a with this command line you see all the processes
$root
new TBrowser()
CCD1->Draw["DiffX:DiffY"] With this command line you can see the plot of x vs y
