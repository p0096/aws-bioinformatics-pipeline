def read_fasta(path):
    sequences = []
    seq = ""
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if seq:
                    sequences.append(seq)
                    seq = ""
            else:
                seq += line
        if seq:
            sequences.append(seq)
    return sequences


def gc_content(seq):
    return (seq.count("G") + seq.count("C")) / len(seq)


seqs = read_fasta("data/sample.fasta")

lengths = [len(s) for s in seqs]
gcs = [gc_content(s) for s in seqs]

with open("results/summary.txt", "w") as out:
    out.write(f"Number of sequences: {len(seqs)}\n")
    out.write(f"Average length: {sum(lengths)/len(lengths):.2f}\n")
    out.write(f"Average GC content: {sum(gcs)/len(gcs):.2f}\n")

print("Analysis finished. Results saved in results/summary.txt")
