---
{
  "projection_kind": "taulib_declaration",
  "title": "MoralMonodromy",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/moral-monodromy/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::MoralMonodromy",
  "declaration_slug": "moral-monodromy",
  "kind": "structure",
  "name": "MoralMonodromy",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 233,
  "source_line_end": 240,
  "registry_ids": [
    "VII.D68"
  ],
  "related_registry_items": [
    {
      "id": "VII.D68",
      "title": "Moral Monodromy",
      "url": "/registry/object/VII.D68/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L233-L240",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L233-L240",
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

- Module: [TauLib.BookVII.Ethics.CIProof](/verify/taulib/docs/book-vii-ethics-ciproof/)
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L233-L240)
- Source range: L233-L240
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D68` — Moral Monodromy

## Immediate Comment / Docstring

```lean
/-- [VII.D68] Moral Monodromy (ch81). For loop γ : U ∼> U in site of
    perspectives, holonomy Hol_M(γ) = M_γ : Max(U) → Max(U).
    Maxim is flat (monodromy-free) iff Hol_M(γ) = Id for all loops. -/
```

## Source Excerpt

```lean
structure MoralMonodromy where
  /-- Holonomy well-defined for all loops. -/
  holonomy_defined : Bool := true
  /-- Can detect non-trivial monodromy. -/
  detects_monodromy : Bool := true
  /-- Flat = monodromy-free. -/
  flat_iff_trivial : Bool := true
  deriving Repr
```
