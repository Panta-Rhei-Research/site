---
{
  "projection_kind": "taulib_declaration",
  "title": "locality_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/locality-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.SheafCoherence`.",
  "declaration_id": "TauLib.BookII.Hartogs.SheafCoherence::locality_check",
  "declaration_slug": "locality-check",
  "kind": "def",
  "name": "locality_check",
  "module_name": "TauLib.BookII.Hartogs.SheafCoherence",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/",
  "source_line_start": 255,
  "source_line_end": 274,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L255-L274",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.SheafCoherence",
        "url": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L255-L274",
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

- Module: [TauLib.BookII.Hartogs.SheafCoherence](/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/)
- Source path: [`TauLib/BookII/Hartogs/SheafCoherence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L255-L274)
- Source range: L255-L274
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.T32, S1] Locality axiom:
    If f restricts to 0 on every cylinder in a covering of Z/P_kZ,
    then f = 0.

    In our setting, the cover is the partition { C_{k,a} | 0 ≤ a < P_k }.
    If f(x) = 0 for all x in each C_{k,a}, then f(x) = 0 for all x.
    This is trivially true because the cylinders cover Z/P_kZ.

    We verify: the cylinders C_{k,0}, ..., C_{k,P_k-1} cover [0, P_k). -/
```

## Source Excerpt

```lean
def locality_check (k_max : TauIdx) : Bool :=
  go_k 1 (k_max * 300 + 1)
where
  go_k (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > k_max then true
    else
      -- Every x in [0, P_k) is covered by some cylinder
      let ok := check_cover 0 (primorial k) k
      ok && go_k (k + 1) (fuel - 1)
  termination_by fuel
  check_cover (x fuel k : Nat) : Bool :=
    if fuel = 0 then true
    else if x >= primorial k then true
    else
      -- x is in C_{k, reduce(x,k)}, and reduce(x,k) < P_k
      let a := reduce x k
      presheaf_assign k a x && (a < primorial k) &&
      check_cover (x + 1) (fuel - 1) k
  termination_by fuel
```
