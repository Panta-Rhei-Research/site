---
{
  "projection_kind": "taulib_declaration",
  "title": "teich_residues",
  "permalink": "/verify/taulib/docs/book-i-polarity-teichmueller-lift/teich-residues/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.TeichmuellerLift`.",
  "declaration_id": "TauLib.BookI.Polarity.TeichmuellerLift::teich_residues",
  "declaration_slug": "teich-residues",
  "kind": "def",
  "name": "teich_residues",
  "module_name": "TauLib.BookI.Polarity.TeichmuellerLift",
  "module_url": "/verify/taulib/docs/book-i-polarity-teichmueller-lift/",
  "source_line_start": 44,
  "source_line_end": 45,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/TeichmuellerLift.lean#L44-L45",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.TeichmuellerLift",
        "url": "/verify/taulib/docs/book-i-polarity-teichmueller-lift/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/TeichmuellerLift.lean#L44-L45",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookI.Polarity.TeichmuellerLift](/verify/taulib/docs/book-i-polarity-teichmueller-lift/)
- Source path: [`TauLib/BookI/Polarity/TeichmuellerLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/TeichmuellerLift.lean#L44-L45)
- Source range: L44-L45
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Teichmüller residue vector: r at position i (0-indexed), 0 elsewhere.
    This is the input to CRT reconstruction for a single-prime lift. -/
```

## Source Excerpt

```lean
def teich_residues (r i k : TauIdx) : List TauIdx :=
  (List.range k).map (fun j => if j == i then r % nth_prime (i + 1) else 0)
```
