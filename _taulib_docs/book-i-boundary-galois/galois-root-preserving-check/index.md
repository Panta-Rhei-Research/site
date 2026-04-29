---
{
  "projection_kind": "taulib_declaration",
  "title": "galois_root_preserving_check",
  "permalink": "/verify/taulib/docs/book-i-boundary-galois/galois-root-preserving-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Galois`.",
  "declaration_id": "TauLib.BookI.Boundary.Galois::galois_root_preserving_check",
  "declaration_slug": "galois-root-preserving-check",
  "kind": "def",
  "name": "galois_root_preserving_check",
  "module_name": "TauLib.BookI.Boundary.Galois",
  "module_url": "/verify/taulib/docs/book-i-boundary-galois/",
  "source_line_start": 138,
  "source_line_end": 162,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Galois.lean#L138-L162",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Galois",
        "url": "/verify/taulib/docs/book-i-boundary-galois/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Galois.lean#L138-L162",
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

- Module: [TauLib.BookI.Boundary.Galois](/verify/taulib/docs/book-i-boundary-galois/)
- Source path: [`TauLib/BookI/Boundary/Galois.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Galois.lean#L138-L162)
- Source range: L138-L162
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.D95a] Check that σ_a preserves roots of unity:
    if z^n ≡ 1 mod m, then (σ_a(z))^n ≡ 1 mod m, where σ_a(z) = z^a. -/
```

## Source Excerpt

```lean
def galois_root_preserving_check (σ : GaloisAut) : Bool :=
  let pk := primorial σ.stage
  go 0 pk pk
where
  go (z pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if z >= pk then true
    else
      -- For each z, check: if z is a root of unity mod pk for some order,
      -- then z^a is also a root of unity of the same order
      let ok := go_n z σ.multiplier 1 pk pk
      ok && go (z + 1) pk (fuel - 1)
  termination_by fuel
  go_n (z a n pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if n > pk then true
    else
      -- If z^n ≡ 1 mod pk, check that (z^a)^n ≡ 1 mod pk
      let is_root := Nat.mod (z ^ n) pk == Nat.mod 1 pk
      let ok := if is_root then
        let za := Nat.mod (z ^ a) pk
        Nat.mod (za ^ n) pk == Nat.mod 1 pk
      else true
      ok && go_n z a (n + 1) pk (fuel - 1)
  termination_by fuel
```
