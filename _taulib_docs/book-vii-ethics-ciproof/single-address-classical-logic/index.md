---
{
  "projection_kind": "taulib_declaration",
  "title": "single_address_classical_logic",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/single-address-classical-logic/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::single_address_classical_logic",
  "declaration_slug": "single-address-classical-logic",
  "kind": "theorem",
  "name": "single_address_classical_logic",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 607,
  "source_line_end": 611,
  "registry_ids": [
    "VII.T22"
  ],
  "related_registry_items": [
    {
      "id": "VII.T22",
      "title": "Single-Address Classical Logic",
      "url": "/registry/object/VII.T22/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L607-L611",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Ethics.CIProof",
        "url": "/verify/taulib/docs/book-vii-ethics-ciproof/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L607-L611",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookVII.Ethics.CIProof](/verify/taulib/docs/book-vii-ethics-ciproof/)
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L607-L611)
- Source range: L607-L611
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T22` — Single-Address Classical Logic

## Immediate Comment / Docstring

```lean
/-- [VII.T22] Single-Address Classical Logic (ch39). At a single
    NF-address, classical logic holds: excluded middle, double
    negation elimination, and all Boolean identities are valid.
    This is the ground level of the scale-dependent logic stack. -/
```

## Source Excerpt

```lean
theorem single_address_classical_logic :
    boolean_micro.single_address = true ∧
    boolean_micro.two_valued = true ∧
    boolean_micro.decidable = true :=
  ⟨rfl, rfl, rfl⟩
```
