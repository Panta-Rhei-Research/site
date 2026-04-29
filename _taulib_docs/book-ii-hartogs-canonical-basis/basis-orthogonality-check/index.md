---
{
  "projection_kind": "taulib_declaration",
  "title": "basis_orthogonality_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/basis-orthogonality-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.CanonicalBasis`.",
  "declaration_id": "TauLib.BookII.Hartogs.CanonicalBasis::basis_orthogonality_check",
  "declaration_slug": "basis-orthogonality-check",
  "kind": "def",
  "name": "basis_orthogonality_check",
  "module_name": "TauLib.BookII.Hartogs.CanonicalBasis",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/",
  "source_line_start": 85,
  "source_line_end": 100,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L85-L100",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L85-L100",
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
- Source path: [`TauLib/BookII/Hartogs/CanonicalBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L85-L100)
- Source range: L85-L100
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.D45, orthogonality] For a fixed stage k and prime p_{prime_idx},
    the generators for distinct residue classes v and w are orthogonal:
    E_{k,p,v}(x) * E_{k,p,w}(x) = 0 for all x when v ≠ w. -/
```

## Source Excerpt

```lean
def basis_orthogonality_check (k_max bound : TauIdx) : Bool :=
  go 1 1 0 0 ((k_max + 1) * (k_max + 1) * (bound + 1))
where
  go (k pi_idx v w fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > k_max then true
    else
      let p := nth_prime pi_idx
      if pi_idx > k then go (k + 1) 1 0 0 (fuel - 1)
      else if p == 0 then go k (pi_idx + 1) 0 0 (fuel - 1)
      else if v >= p then go k (pi_idx + 1) 0 0 (fuel - 1)
      else if w >= p then go k pi_idx (v + 1) 0 (fuel - 1)
      else if v == w then go k pi_idx v (w + 1) (fuel - 1)
      else
        ortho_pair k pi_idx v w && go k pi_idx v (w + 1) (fuel - 1)
  termination_by fuel
```
