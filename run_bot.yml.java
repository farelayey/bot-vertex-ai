name: Generate Images Daily

on:
  # Ini adalah pemicu. Bot akan jalan jika:
  # 1. Anda menjalankannya manual (workflow_dispatch)
  # 2. Sesuai jadwal setiap jam 8 pagi WIB (cron: '0 1 * * *')
  workflow_dispatch:
  schedule:
    - cron: '0 1 * * *'

jobs:
  build_and_commit:
    runs-on: ubuntu-latest
    steps:
      - name: 1. Checkout Repository
        uses: actions/checkout@v3

      - name: 2. Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: 3. Install Dependencies
        run: pip install google-cloud-aiplatform Pillow

      - name: 4. Authenticate with Google Cloud
        uses: 'google-github-actions/auth@v1'
        with:
          credentials_json: '${{ secrets.GCP_SA_KEY }}'

      - name: 5. Run Python Script to Generate Images
        run: python bot.py

      - name: 6. Commit and Push Generated Images
        run: |
          git config --global user.name 'github-actions[bot]'
          git config --global user.email 'github-actions[bot]@users.noreply.github.com'
          git pull
          git add *.png || echo "Tidak ada gambar baru untuk ditambahkan."
          # Hanya commit jika ada perubahan
          git diff --quiet && git diff --staged --quiet || git commit -m "🤖 Bot: Menambahkan gambar baru yang dibuat secara otomatis"
          git push
import android.app.Activity;
import android.os.Bundle;

public class run_bot.yml {
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }
    
}