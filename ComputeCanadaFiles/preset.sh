# To run this, use `sh preset.sh`

module load python/3.8
module load scipy-stack
python -c "print('Python is working!')"
if python -c "import mne" &> /dev/null; then
    echo "MNE is installed."
else
    echo "MNE is not working properly"
fi