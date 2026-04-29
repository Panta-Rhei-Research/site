---
{
  "projection_kind": "taulib_declaration",
  "title": "randomness_as_internal_complexity",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/randomness-as-internal-complexity/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::randomness_as_internal_complexity",
  "declaration_slug": "randomness-as-internal-complexity",
  "kind": "theorem",
  "name": "randomness_as_internal_complexity",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 672,
  "source_line_end": 675,
  "registry_ids": [
    "VII.P15"
  ],
  "related_registry_items": [
    {
      "id": "VII.P15",
      "title": "Randomness as Internal Complexity",
      "url": "/registry/object/VII.P15/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L672-L675",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L672-L675",
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
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L672-L675)
- Source range: L672-L675
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.P15` — Randomness as Internal Complexity

## Immediate Comment / Docstring

```lean
/-- [VII.P15] Randomness as Internal Complexity (ch40). What appears
    random is structurally complex: Kolmogorov incompressibility is
    the criterion. No dice-rolling deity needed. -/
```

## Source Excerpt

```lean
theorem randomness_as_internal_complexity :
    internal_randomness.no_external_source = true ∧
    internal_randomness.complexity_as_randomness = true :=
  ⟨rfl, rfl⟩
```
