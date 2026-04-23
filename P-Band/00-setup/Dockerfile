FROM continuumio/miniconda3:latest

WORKDIR /workspace

COPY environment.yml .
RUN conda env create -f environment.yml && conda clean -afy

SHELL ["conda", "run", "-n", "p-band-sar", "/bin/bash", "-c"]

COPY .. /workspace/

EXPOSE 8888

CMD ["conda", "run", "--no-capture-output", "-n", "p-band-sar", \
     "jupyter", "lab", "--ip=0.0.0.0", "--port=8888", \
     "--no-browser", "--allow-root"]
