---
{
  "projection_kind": "taulib_declaration",
  "title": "capstone_combines_three",
  "permalink": "/corpus/taulib/docs/book-v-coda-hermetic-closure/capstone-combines-three/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Coda.HermeticClosure`.",
  "declaration_id": "TauLib.BookV.Coda.HermeticClosure::capstone_combines_three",
  "declaration_slug": "capstone-combines-three",
  "kind": "theorem",
  "name": "capstone_combines_three",
  "module_name": "TauLib.BookV.Coda.HermeticClosure",
  "module_url": "/corpus/taulib/docs/book-v-coda-hermetic-closure/",
  "source_line_start": 373,
  "source_line_end": 378,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L373-L378",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.HermeticClosure",
        "url": "/corpus/taulib/docs/book-v-coda-hermetic-closure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L373-L378",
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

- Module: [TauLib.BookV.Coda.HermeticClosure](/corpus/taulib/docs/book-v-coda-hermetic-closure/)
- Source path: [`TauLib/BookV/Coda/HermeticClosure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L373-L378)
- Source range: L373-L378
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Capstone: V.T162 combines V.T159 (identity) + V.T160 (self-description) + V.T161 (closure). -/
```

## Source Excerpt

```lean
theorem capstone_combines_three :
    hermetic_identity.decomp_exact = true ∧
    self_description.self_description_exact = true ∧
    hermetic_closure.observer_conditions = true ∧
    hermetic_truth_complete.single_object = true :=
  ⟨rfl, rfl, rfl, rfl⟩
```
