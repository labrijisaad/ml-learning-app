# Machine Learning App

## Getting Started

Welcome to the test Machine Learning App! Whether you prefer local development or containerized deployment, getting started is a breeze.

### Local Development

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create .env File:**
   - Copy `.env.template` to `.env`
   - Update the necessary environment variables in the newly created `.env` file.

3. **Set Up Virtual Environment:**
   ```bash
   make venv-setup
   ```

4. **Install Dependencies:**
   ```bash
   make venv-install
   ```

5. **Run the Application:**
   ```bash
   make local-run
   ```

### Containerized Deployment with Docker

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create .env File:**
   - Copy `.env.template` to `.env`
   - Update the necessary environment variables in the newly created `.env` file.

3. **Build and Run Docker Container:**
   ```bash
   make all-docker
   ```

4. **Clean Up (Optional):**
   ```bash
   make clean
   ```

Now you're ready to analyze sentiments with ease using the Sentiment Analysis App! 🚀📊