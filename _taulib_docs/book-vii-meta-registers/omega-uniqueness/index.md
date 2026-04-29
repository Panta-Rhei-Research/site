---
{
  "projection_kind": "taulib_declaration",
  "title": "omega_uniqueness",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/omega-uniqueness/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::omega_uniqueness",
  "declaration_slug": "omega-uniqueness",
  "kind": "theorem",
  "name": "omega_uniqueness",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 998,
  "source_line_end": 1004,
  "registry_ids": [
    "VII.T16"
  ],
  "related_registry_items": [
    {
      "id": "VII.T16",
      "title": "ω-Uniqueness",
      "url": "/registry/object/VII.T16/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L998-L1004",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Registers",
        "url": "/verify/taulib/docs/book-vii-meta-registers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L998-L1004",
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

- Module: [TauLib.BookVII.Meta.Registers](/verify/taulib/docs/book-vii-meta-registers/)
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L998-L1004)
- Source range: L998-L1004
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T16` — ω-Uniqueness

## Immediate Comment / Docstring

```lean
/-- [VII.T16] ω-Uniqueness (ch32). Categorical proof: if T₁ and T₂
    are both terminal, then T₁ ≅ T₂ via unique isomorphism.
    Applied to ω: the closure generator is unique. -/
```

## Source Excerpt

```lean
theorem omega_uniqueness :
    omega_uniqueness_principle.terminal = true ∧
    omega_uniqueness_principle.unique_up_to_iso = true ∧
    omega_uniqueness_principle.structurally_determined = true :=
  ⟨rfl, rfl, rfl⟩

end Tau.BookVII.Meta.Registers
```
