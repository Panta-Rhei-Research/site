---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L230",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-majorana-structure/eval-l230/",
  "summary_short": "`eval` declaration in `TauLib.BookIV.Electroweak.MajoranaStructure`.",
  "declaration_id": "TauLib.BookIV.Electroweak.MajoranaStructure::#eval:230",
  "declaration_slug": "eval-l230",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookIV.Electroweak.MajoranaStructure",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-majorana-structure/",
  "source_line_start": 230,
  "source_line_end": 233,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L230-L233",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.MajoranaStructure",
        "url": "/verify/taulib/docs/book-iv-electroweak-majorana-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L230-L233",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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

- Module: [TauLib.BookIV.Electroweak.MajoranaStructure](/verify/taulib/docs/book-iv-electroweak-majorana-structure/)
- Source path: [`TauLib/BookIV/Electroweak/MajoranaStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L230-L233)
- Source range: L230-L233
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- (5, 1, 1, 5): chi_plus(z)=5=chi_minus(sigma(z)), chi_minus(z)=1=chi_plus(sigma(z)) ✓

-- Verify sigma reverses charge
```

## Source Excerpt

```lean
#eval let z : SplitComplex := ⟨3, 2⟩
      let q_z := chi_plus_val z - chi_minus_val z   -- = 5 - 1 = 4
      let q_sz := chi_plus_val (polarity_inv z) - chi_minus_val (polarity_inv z)  -- = 1 - 5 = -4
      (q_z, q_sz)  -- (4, -4): charge reversed ✓
```
