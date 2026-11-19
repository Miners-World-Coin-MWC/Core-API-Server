
module.exports = {
  apps: [
    {
      name: "mwc-api-mainnet",
      cwd: "/home/crypto/api-server",
      script: "/home/crypto/api-server/venv/bin/gunicorn",
      interpreter: "/home/crypto/api-server/venv/bin/python3.8",
      args: [
        "-b",
        "0.0.0.0:1234",
        "server:app"
      ],
      exec_mode: "fork",
      instances: 1,
      autorestart: true,
      watch: false,
      max_memory_restart: "500M",
      time: true,
      merge_logs: true,
      out_file: "/home/crypto/api-server/logs/pm2-out.log",
      error_file: "/home/crypto/api-server/logs/pm2-error.log"
    }
  ]
};

