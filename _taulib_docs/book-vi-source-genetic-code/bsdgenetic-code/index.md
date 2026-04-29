---
{
  "projection_kind": "taulib_declaration",
  "title": "BSDGeneticCode",
  "permalink": "/verify/taulib/docs/book-vi-source-genetic-code/bsdgenetic-code/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Source.GeneticCode`.",
  "declaration_id": "TauLib.BookVI.Source.GeneticCode::BSDGeneticCode",
  "declaration_slug": "bsdgenetic-code",
  "kind": "structure",
  "name": "BSDGeneticCode",
  "module_name": "TauLib.BookVI.Source.GeneticCode",
  "module_url": "/verify/taulib/docs/book-vi-source-genetic-code/",
  "source_line_start": 38,
  "source_line_end": 53,
  "registry_ids": [
    "VI.D40"
  ],
  "related_registry_items": [
    {
      "id": "VI.D40",
      "title": "BSD Motivic Structure of the Genetic Code",
      "url": "/registry/object/VI.D40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/GeneticCode.lean#L38-L53",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Source.GeneticCode",
        "url": "/verify/taulib/docs/book-vi-source-genetic-code/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/GeneticCode.lean#L38-L53",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookVI.Source.GeneticCode](/verify/taulib/docs/book-vi-source-genetic-code/)
- Source path: [`TauLib/BookVI/Source/GeneticCode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/GeneticCode.lean#L38-L53)
- Source range: L38-L53
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D40` — BSD Motivic Structure of the Genetic Code

## Immediate Comment / Docstring

```lean
/-- [VI.D40] BSD Motivic Structure of the Genetic Code.
    The 20 standard amino acids and 64 codons reflect
    BSD-force structure (Book III, Part V) on the carrier's code space.
    Degeneracy pattern = error-correcting code. -/
```

## Source Excerpt

```lean
structure BSDGeneticCode where
  /-- Number of standard amino acids. -/
  amino_acids : Nat
  /-- Exactly 20. -/
  aa_eq : amino_acids = 20
  /-- Number of codons. -/
  codons : Nat
  /-- Exactly 64 = 4³. -/
  codons_eq : codons = 64
  /-- Stop codons. -/
  stop_codons : Nat
  /-- Exactly 3 stop codons. -/
  stop_eq : stop_codons = 3
  /-- Connected to BSD force (Book III, Part V). -/
  bsd_connection : Bool := true
  deriving Repr
```
