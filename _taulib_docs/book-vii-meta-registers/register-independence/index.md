---
{
  "projection_kind": "taulib_declaration",
  "title": "register_independence",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/register-independence/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::register_independence",
  "declaration_slug": "register-independence",
  "kind": "theorem",
  "name": "register_independence",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 174,
  "source_line_end": 183,
  "registry_ids": [
    "VII.T01"
  ],
  "related_registry_items": [
    {
      "id": "VII.T01",
      "title": "Register Independence Theorem",
      "url": "/registry/object/VII.T01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L174-L183",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L174-L183",
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
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L174-L183)
- Source range: L174-L183
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T01` — Register Independence Theorem

## Immediate Comment / Docstring

```lean
/-- [VII.T01] Register Independence: incoherence in one register does not
    entail incoherence in any other. Four readout functors have pairwise
    distinct codomains (Obs, Norm, Proof, Stance) with no coherence-propagating
    natural transformations.

    Exception: S_L where Reg_D and Reg_C coincide.

    Computational verification: each pair of pure registers has distinct
    codomain categories (4 codomains, C(4,2) = 6 pairs, all independent). -/
```

## Source Excerpt

```lean
theorem register_independence :
    pure_register_pair_count = 6 ∧
    canonical_decomposition.pure_count = 4 ∧
    reg_E.register_type ≠ reg_P.register_type ∧
    reg_E.register_type ≠ reg_D.register_type ∧
    reg_E.register_type ≠ reg_C.register_type ∧
    reg_P.register_type ≠ reg_D.register_type ∧
    reg_P.register_type ≠ reg_C.register_type ∧
    reg_D.register_type ≠ reg_C.register_type :=
  ⟨rfl, rfl, by decide, by decide, by decide, by decide, by decide, by decide⟩
```
