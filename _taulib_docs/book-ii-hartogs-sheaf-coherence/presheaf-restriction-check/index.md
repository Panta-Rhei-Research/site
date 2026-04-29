---
{
  "projection_kind": "taulib_declaration",
  "title": "presheaf_restriction_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/presheaf-restriction-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.SheafCoherence`.",
  "declaration_id": "TauLib.BookII.Hartogs.SheafCoherence::presheaf_restriction_check",
  "declaration_slug": "presheaf-restriction-check",
  "kind": "def",
  "name": "presheaf_restriction_check",
  "module_name": "TauLib.BookII.Hartogs.SheafCoherence",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/",
  "source_line_start": 105,
  "source_line_end": 122,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L105-L122",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L105-L122",
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
- Source path: [`TauLib/BookII/Hartogs/SheafCoherence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L105-L122)
- Source range: L105-L122
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Restriction compatibility: restricting from stage l to k and then
    from k to j equals restricting directly from l to j.
    This is tower coherence applied to the restriction maps. -/
```

## Source Excerpt

```lean
def presheaf_restriction_check (k_max bound : TauIdx) : Bool :=
  go 0 1 1 ((k_max + 1) * (k_max + 1) * (bound + 1))
where
  go (a j k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if a > bound then true
    else if j > k_max then go (a + 1) 1 1 (fuel - 1)
    else if k > k_max then go a (j + 1) (j + 1) (fuel - 1)
    else
      let l := k_max
      if j ≤ k && k ≤ l then
        let r_lk := presheaf_restrict a l k
        let r_kj := presheaf_restrict r_lk k j
        let r_lj := presheaf_restrict a l j
        (r_kj == r_lj) && go a j (k + 1) (fuel - 1)
      else
        go a j (k + 1) (fuel - 1)
  termination_by fuel
```
