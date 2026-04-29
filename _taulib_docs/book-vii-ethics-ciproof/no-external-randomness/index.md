---
{
  "projection_kind": "taulib_declaration",
  "title": "no_external_randomness",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/no-external-randomness/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::no_external_randomness",
  "declaration_slug": "no-external-randomness",
  "kind": "theorem",
  "name": "no_external_randomness",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 685,
  "source_line_end": 688,
  "registry_ids": [
    "VII.T24"
  ],
  "related_registry_items": [
    {
      "id": "VII.T24",
      "title": "No External Randomness",
      "url": "/registry/object/VII.T24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L685-L688",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L685-L688",
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
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L685-L688)
- Source range: L685-L688
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T24` — No External Randomness

## Immediate Comment / Docstring

```lean
/-- [VII.T24] No External Randomness (ch40). There is no external
    random number generator: NF-addressability precludes any source
    outside the kernel. All stochastic behaviour is projective
    (coarse-graining of deterministic dynamics). -/
```

## Source Excerpt

```lean
theorem no_external_randomness :
    internal_randomness.no_external_source = true ∧
    internal_randomness.deterministic_kernel = true :=
  ⟨rfl, rfl⟩
```
