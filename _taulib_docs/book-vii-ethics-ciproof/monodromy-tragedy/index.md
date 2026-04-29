---
{
  "projection_kind": "taulib_declaration",
  "title": "monodromy_tragedy",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/monodromy-tragedy/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::monodromy_tragedy",
  "declaration_slug": "monodromy-tragedy",
  "kind": "theorem",
  "name": "monodromy_tragedy",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 249,
  "source_line_end": 253,
  "registry_ids": [
    "VII.T33"
  ],
  "related_registry_items": [
    {
      "id": "VII.T33",
      "title": "Monodromy as Source of Tragedy",
      "url": "/registry/object/VII.T33/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L249-L253",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L249-L253",
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
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L249-L253)
- Source range: L249-L253
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T33` — Monodromy as Source of Tragedy

## Immediate Comment / Docstring

```lean
/-- [VII.T33] Monodromy as Source of Tragedy (ch81). Four claims:
    (1) Local consistency: each Max(U_i) ≠ ∅
    (2) Global non-closure: Hol_M(γ) ≠ Id, no single global enactment
    (3) Topological, not logical: obstruction in π₁(P, U) → Aut(Max(U))
    (4) Locatability: specific overlap where transported enactments disagree -/
```

## Source Excerpt

```lean
theorem monodromy_tragedy :
    moral_monodromy.holonomy_defined = true ∧
    moral_monodromy.detects_monodromy = true ∧
    moral_monodromy.flat_iff_trivial = true :=
  ⟨rfl, rfl, rfl⟩
```
