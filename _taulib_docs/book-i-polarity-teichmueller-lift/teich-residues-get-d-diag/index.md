---
{
  "projection_kind": "taulib_declaration",
  "title": "teich_residues_getD_diag",
  "permalink": "/corpus/taulib/docs/book-i-polarity-teichmueller-lift/teich-residues-get-d-diag/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.TeichmuellerLift`.",
  "declaration_id": "TauLib.BookI.Polarity.TeichmuellerLift::teich_residues_getD_diag",
  "declaration_slug": "teich-residues-get-d-diag",
  "kind": "theorem",
  "name": "teich_residues_getD_diag",
  "module_name": "TauLib.BookI.Polarity.TeichmuellerLift",
  "module_url": "/corpus/taulib/docs/book-i-polarity-teichmueller-lift/",
  "source_line_start": 197,
  "source_line_end": 200,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/TeichmuellerLift.lean#L197-L200",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.TeichmuellerLift",
        "url": "/corpus/taulib/docs/book-i-polarity-teichmueller-lift/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/TeichmuellerLift.lean#L197-L200",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Polarity.TeichmuellerLift](/corpus/taulib/docs/book-i-polarity-teichmueller-lift/)
- Source path: [`TauLib/BookI/Polarity/TeichmuellerLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/TeichmuellerLift.lean#L197-L200)
- Source range: L197-L200
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Helper: teich_residues diagonal — getD at position i = r % p_{i+1}. -/
```

## Source Excerpt

```lean
private theorem teich_residues_getD_diag {r i k : TauIdx} (hi : i < k) :
    (teich_residues r i k).getD i 0 = r % nth_prime (i + 1) := by
  simp only [teich_residues, List.getD, List.getElem?_map,
    List.getElem?_range hi, Option.map, Option.getD_some, beq_self_eq_true, ↓reduceIte]
```
