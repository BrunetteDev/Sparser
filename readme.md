# Sparser

CLI program to compress and reconstruct a vector (linear or matrix) using the mathematical method *Compressed Sensing* created by Terence Tao.

## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

- Python 3.11 (or later)
### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/migueldeltorodev/innovasoft-test
   ```

2. Navigate to the project directory:
   ```bash
   cd your-repo-name
   ```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```



### Running the Application

#### Parameters (Flags):

- `-m Number of rows of the compresion matrix`
- `-n Number of columns of the compresion matrix`
- `-cr Compresion Ratio (0-1)`
- `-mc Use the multicol of the file (0-False 1-True)`
- `-b Base of Data Representation (0-Fourier 1-Haar Wavelet 2-Discrete Cosine)`
- `-ic Initial Value of the slide of the column of the data to process`
- `-lc Last value of the slide of the column of the data to process`
- `-p Path of file to process`
- `-ps Path to save the results`
#### Example:

`python main.py -n 11968 -cr 0.5 -b 0 -mc 1 -ic 1 -lc 2 -p <path> -ps <path save>'`

## Project Structure

```
src/
  ├── Files/         # Exported Data 
  ├── methods/       # Mathematical Methods
  ├── main.py        # Main App 
  └── metaclass.py   # Class to handle the runner 
```

## Dependencies

- pandas
- matplotlib
- cvxpy

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.