---
{
  "projection_kind": "taulib_declaration",
  "title": "basis_completeness_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/basis-completeness-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.CanonicalBasis`.",
  "declaration_id": "TauLib.BookII.Hartogs.CanonicalBasis::basis_completeness_check",
  "declaration_slug": "basis-completeness-check",
  "kind": "def",
  "name": "basis_completeness_check",
  "module_name": "TauLib.BookII.Hartogs.CanonicalBasis",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/",
  "source_line_start": 124,
  "source_line_end": 135,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L124-L135",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.CanonicalBasis",
        "url": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L124-L135",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookII.Hartogs.CanonicalBasis](/verify/taulib/docs/book-ii-hartogs-canonical-basis/)
- Source path: [`TauLib/BookII/Hartogs/CanonicalBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L124-L135)
- Source range: L124-L135
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.D45, completeness] For a fixed stage k and prime p_{prime_idx},
    sum_{v=0}^{p-1} E_{k,p,v}(x) = 1 for all x. -/
```

## Source Excerpt

```lean
def basis_completeness_check (k_max bound : TauIdx) : Bool :=
  go 1 1 0 ((k_max + 1) * (k_max + 1) * (bound + 1))
where
  go (k pi_idx x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > k_max then true
    else if pi_idx > k then go (k + 1) 1 0 (fuel - 1)
    else if x >= primorial k then go k (pi_idx + 1) 0 (fuel - 1)
    else
      let s := gen_sum k pi_idx x
      (s == 1) && go k pi_idx (x + 1) (fuel - 1)
  termination_by fuel
```
