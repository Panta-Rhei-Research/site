---
{
  "projection_kind": "taulib_declaration",
  "title": "truth_4_paraconsistency",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/truth-4-paraconsistency/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::truth_4_paraconsistency",
  "declaration_slug": "truth-4-paraconsistency",
  "kind": "theorem",
  "name": "truth_4_paraconsistency",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 898,
  "source_line_end": 904,
  "registry_ids": [
    "VII.L10"
  ],
  "related_registry_items": [
    {
      "id": "VII.L10",
      "title": "Truth4 Paraconsistency",
      "url": "/registry/object/VII.L10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L898-L904",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L898-L904",
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
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L898-L904)
- Source range: L898-L904
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.L10` — Truth4 Paraconsistency

## Immediate Comment / Docstring

```lean
/-- [VII.L10] Truth-4 Paraconsistency (ch44). At the boundary,
    a 4-valued truth system: {true, false, both, neither}.
    "Both" = φ true in one register, ¬φ true in another.
    "Neither" = φ undecided in all registers.
    The 4-valued system is consistent with scale-dependent logic. -/
```

## Source Excerpt

```lean
theorem truth_4_paraconsistency :
    paraconsistent.controlled_contradiction = true ∧
    paraconsistent.no_explosion = true ∧
    boolean_micro.two_valued = true :=
  ⟨rfl, rfl, rfl⟩

end Tau.BookVII.Ethics.CIProof
```
